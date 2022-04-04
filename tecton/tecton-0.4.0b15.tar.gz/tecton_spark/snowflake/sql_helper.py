import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Union

import pandas
import pendulum
import sqlparse

from tecton_proto.common import aggregation_function_pb2 as afpb
from tecton_proto.data.feature_view_pb2 import FeatureView as FeatureViewProto
from tecton_proto.data.feature_view_pb2 import NewTemporalAggregate
from tecton_spark import conf
from tecton_spark import errors
from tecton_spark import time_utils
from tecton_spark.feature_definition_wrapper import FeatureDefinitionWrapper as FeatureDefinition
from tecton_spark.feature_set_config import FeatureSetConfig
from tecton_spark.snowflake.errors import TectonSnowflakeNotImplementedError
from tecton_spark.snowflake.pipeline_helper import pipeline_to_df_with_input
from tecton_spark.snowflake.pipeline_helper import pipeline_to_sql_string
from tecton_spark.snowflake.templates_utils import load_template

TEMP_SPINE_TABLE_NAME = "_TEMP_SPINE_TABLE_FROM_DF"

HISTORICAL_FEATURES_TEMPLATE = load_template("historical_features.sql")
MATERIALIZATION_TILE_TEMPLATE = load_template("materialization_tile.sql")
MATERIALIZATION_TEMPLATE = load_template("materialization.sql")
TIME_LIMIT_TEMPLATE = load_template("time_limit.sql")
FULL_AGGREGATION_TEMPLATE = load_template("run_full_aggregation.sql")
PARTIAL_AGGREGATION_TEMPLATE = load_template("run_partial_aggregation.sql")
ONLINE_STORE_COPIER_TEMPLATE = load_template("online_store_copier.sql")

# TODO(TEC-6204): Last and LastN are not currently supported
#
# Map of proto function type -> set of (output column prefix, snowflake function name)
AGGREGATION_PLANS = {
    afpb.AGGREGATION_FUNCTION_SUM: {("SUM", "SUM")},
    afpb.AGGREGATION_FUNCTION_MIN: {("MIN", "MIN")},
    afpb.AGGREGATION_FUNCTION_MAX: {("MAX", "MAX")},
    afpb.AGGREGATION_FUNCTION_COUNT: {("COUNT", "COUNT")},
    afpb.AGGREGATION_FUNCTION_MEAN: {("COUNT", "COUNT"), ("MEAN", "AVG")},
}


def _format_sql(sql_str: str) -> str:
    return sqlparse.format(sql_str, reindent=True, keyword_case="upper")


@dataclass
class _FeatureSetItemInput:
    """A simplified version of FeatureSetItem which is passed to the SQL template."""

    name: str
    timestamp_key: str
    join_keys: Dict[str, str]
    features: List[str]
    sql: str
    aggregation: Optional[NewTemporalAggregate]
    ttl_seconds: Optional[int]


def _generate_historical_features_sql(
    spine_sql: str,
    feature_set_config: FeatureSetConfig,
    timestamp_key: str,
    from_registered_view: bool,
    include_feature_view_timestamp_columns: bool = False,
    # Whether to use the registered snowflake view for features.
) -> str:
    if include_feature_view_timestamp_columns:
        # TODO(TEC-7238): Implement this
        raise TectonSnowflakeNotImplementedError(
            "include_feature_view_timestamp_columns is not implemented for Snowflake"
        )
    feature_set_items = feature_set_config._get_feature_definitions_and_join_configs()
    input_items = []
    for item in feature_set_items:
        fd = item.feature_definition
        if fd.is_on_demand and not conf.get_or_none("ALPHA_SNOWFLAKE_SNOWPARK_ENABLED"):
            raise TectonSnowflakeNotImplementedError("On-demand features are only supported with Snowpark enabled")
        feature_view = fd.fv
        # Change the feature view name if it's for internal udf use.
        if item.namespace.startswith("_udf_internal"):
            name = item.namespace.upper()
        else:
            name = fd.name

        if not fd.is_on_demand:
            join_keys = {key: value for key, value in item.join_keys}
            features = [
                col_name
                for col_name in fd.view_schema.column_names()
                if col_name not in (list(join_keys.keys()) + [fd.timestamp_key])
            ]
            if len(fd.online_serving_index.join_keys) != len(fd.join_keys):
                raise TectonSnowflakeNotImplementedError("Wildcard is not supported for Snowflake")
            sql_str = generate_run_batch_sql(fd, fd.start_timestamp, spine=spine_sql, spine_timestamp_key=timestamp_key)
            input_items.append(
                _FeatureSetItemInput(
                    name=name,
                    timestamp_key=fd.timestamp_key,
                    join_keys=join_keys,
                    features=features,
                    sql=sql_str,
                    aggregation=(
                        feature_view.temporal_aggregate if feature_view.HasField("temporal_aggregate") else None
                    ),
                    ttl_seconds=(int(fd.serving_ttl.total_seconds()) if fd.is_temporal else None),
                )
            )
    sql_str = HISTORICAL_FEATURES_TEMPLATE.render(
        feature_set_items=input_items,
        spine_timestamp_key=timestamp_key,
        spine_sql=spine_sql,
        include_feature_view_timestamp_columns=include_feature_view_timestamp_columns,
    )

    return sql_str


def get_historical_features(
    spine: Union[pandas.DataFrame, str],
    connection: "snowflake.connector.Connection",
    feature_set_config: FeatureSetConfig,
    timestamp_key: str,
    include_feature_view_timestamp_columns: bool = False,
    # Whether to use the registered snowflake view for features.
    from_registered_view: bool = False,
) -> pandas.DataFrame:
    cur = connection.cursor()
    if isinstance(spine, str):
        spine_sql = spine
    elif isinstance(spine, pandas.DataFrame):
        spine_sql = generate_sql_table_from_pandas_df(df=spine, table_name=TEMP_SPINE_TABLE_NAME, connection=connection)

    sql_str = _generate_historical_features_sql(
        spine_sql=spine_sql,
        feature_set_config=feature_set_config,
        timestamp_key=timestamp_key,
        include_feature_view_timestamp_columns=include_feature_view_timestamp_columns,
        from_registered_view=from_registered_view,
    )
    cur.execute(sql_str)
    return cur.fetch_pandas_all()


def generate_sql_table_from_pandas_df(
    df: pandas.DataFrame,
    table_name: str,
    session: "snowflake.snowpark.Session" = None,
    connection: "snowflake.connector.Connection" = None,
) -> str:
    """Generate a TABLE from pandas.DataFrame. Returns the sql query to select * from the table"""
    if session is None and connection is None:
        raise ValueError("Either session or connection must be provided")

    if session is not None:
        session.sql(f"DROP TABLE IF EXISTS {table_name}").collect()
        session.write_pandas(df, table_name, auto_create_table=True, create_temp_table=True)
        return f"SELECT * FROM {table_name}"

    if connection is not None:
        from snowflake.connector.pandas_tools import write_pandas

        # Get the SQL that would be generated by the create table statement
        create_table_sql = pandas.io.sql.get_schema(df, table_name)

        # Replace the `CREATE TABLE` with `CREATE OR REPLACE TEMPORARY TABLE`
        create_tmp_table_sql = re.sub("^(CREATE TABLE)?", "CREATE OR REPLACE TEMPORARY TABLE", create_table_sql)
        cur = connection.cursor()
        cur.execute(create_tmp_table_sql)
        write_pandas(conn=connection, df=df, table_name=table_name)
        return f"SELECT * FROM {table_name}"


def validate_spine_dataframe(spine_df: "snowflake.snowpark.DataFrame", timestamp_key: str, join_keys: List[str]):
    if timestamp_key not in spine_df.columns:
        raise errors.TectonValidationError(
            f"Expected to find '{timestamp_key}' among available spine columns: '{', '.join(spine_df.columns)}'."
        )
    for field in spine_df.schema.fields:
        if field.name == timestamp_key and field.datatype.type_name != "Timestamp":
            raise errors.TectonValidationError(
                f"Invalid type of timestamp_key column in the given spine. Expected Timestamp, got {field.datatype}"
            )
    for key in join_keys:
        if key not in spine_df.columns:
            raise errors.TectonValidationError(
                f"Expected to find '{key}' among available spine columns: '{', '.join(spine_df.columns)}'."
            )


def get_historical_features_with_snowpark(
    spine: Union[pandas.DataFrame, str, "snowflake.snowpark.DataFrame"],
    session: "snowflake.snowpark.Session",
    feature_set_config: FeatureSetConfig,
    timestamp_key: str,
    include_feature_view_timestamp_columns: bool = False,
    # Whether to use the registered snowflake view for features.
    from_registered_view: bool = False,
) -> "snowflake.snowpark.DataFrame":
    from snowflake.snowpark import DataFrame

    if isinstance(spine, str):
        spine_sql = spine
    elif isinstance(spine, DataFrame):
        spine.write.save_as_table(TEMP_SPINE_TABLE_NAME, mode="overwrite", create_temp_table=True)
        spine_sql = f"SELECT * FROM {TEMP_SPINE_TABLE_NAME}"
    elif isinstance(spine, pandas.DataFrame):
        spine_sql = generate_sql_table_from_pandas_df(df=spine, table_name=TEMP_SPINE_TABLE_NAME, session=session)

    join_keys = [join_key for fd in feature_set_config.feature_definitions for join_key in fd.join_keys]
    validate_spine_dataframe(session.sql(spine_sql), timestamp_key, join_keys=join_keys)

    sql_str = _generate_historical_features_sql(
        spine_sql=spine_sql,
        feature_set_config=feature_set_config,
        timestamp_key=timestamp_key,
        include_feature_view_timestamp_columns=include_feature_view_timestamp_columns,
        from_registered_view=from_registered_view,
    )
    output_df = session.sql(sql_str)

    # Apply ODFV to the spine
    for item in feature_set_config._get_feature_definitions_and_join_configs():
        fd = item.feature_definition
        if fd.is_on_demand:
            view_schema = fd.view_schema
            schema_dict = {col_name: view_schema.spark_type(col_name) for col_name in view_schema.column_names()}
            output_df = pipeline_to_df_with_input(
                session=session,
                input_df=output_df,
                pipeline=fd.pipeline,
                transformations=fd.transformations,
                output_schema=schema_dict,
                name=fd.name,
                fv_id=fd.id,
            )
    columns_to_drop = [column for column in output_df.columns if "_UDF_INTERNAL_" in column]
    if len(columns_to_drop) > 0:
        output_df = output_df.drop(*columns_to_drop)
    return output_df


def generate_run_batch_sql(
    feature_definition: FeatureDefinition,
    # start is inclusive and end is exclusive
    feature_start_time: Union[pendulum.DateTime, datetime] = None,
    feature_end_time: Union[pendulum.DateTime, datetime] = None,
    aggregation_level: str = "full",
    # If spine is provided, it will be used to join with the output results.
    # Currently only work with full aggregation.
    spine: str = None,
    spine_timestamp_key: str = None,
    # Whether to use the registered snowflake view for features.
    from_registered_view: bool = False,
    mock_sql_inputs: Dict[str, str] = None,
) -> str:
    feature_view = feature_definition.feature_view_proto
    # Smart default feature_start_time and feature_end_time if unset.
    if feature_end_time is None:
        feature_end_time = pendulum.now()
    if feature_start_time is None:
        schedule_interval = time_utils.proto_to_duration(feature_view.materialization_params.schedule_interval)
        feature_start_time = feature_end_time - schedule_interval
    if from_registered_view and mock_sql_inputs is None:
        source = f"SELECT * FROM {feature_view.snowflake_data.snowflake_view_name}"
    else:
        source = pipeline_to_sql_string(
            pipeline=feature_definition.pipeline,
            data_sources=feature_definition.data_sources,
            transformations=feature_definition.transformations,
            mock_sql_inputs=mock_sql_inputs,
        )
    if feature_view.HasField("temporal_aggregate"):
        if aggregation_level == "full":
            aggregated_tiles_sql_str = get_materialization_query(
                feature_view=feature_view,
                time_limits=pendulum.period(feature_start_time, feature_end_time),
            )
            aggregated_sql_str = FULL_AGGREGATION_TEMPLATE.render(
                source=aggregated_tiles_sql_str,
                join_keys=list(feature_view.join_keys),
                aggregation=feature_view.temporal_aggregate,
                timestamp_key=feature_view.timestamp_key,
                name=feature_view.fco_metadata.name,
                spine=spine,
                spine_timestamp_key=spine_timestamp_key,
            )
            return _format_sql(aggregated_sql_str)
        elif aggregation_level == "partial":
            aggregated_tiles_sql_str = get_materialization_query(
                feature_view=feature_view,
                time_limits=pendulum.period(feature_start_time, feature_end_time),
                source=source,
            )
            # Rename the output columns, and add tile start/end time columns
            partial_aggregated_sql_str = PARTIAL_AGGREGATION_TEMPLATE.render(
                source=aggregated_tiles_sql_str,
                join_keys=list(feature_view.join_keys),
                aggregations=_get_feature_view_aggregations(feature_view),
                slide_interval=feature_view.temporal_aggregate.slide_interval,
                slide_interval_string=feature_view.temporal_aggregate.slide_interval_string,
                timestamp_key=feature_view.timestamp_key,
            )
            return _format_sql(partial_aggregated_sql_str)
        elif aggregation_level == "disabled":
            sql_str = TIME_LIMIT_TEMPLATE.render(
                source=source,
                timestamp_key=feature_view.timestamp_key,
                start_time=feature_start_time,
                end_time=feature_end_time,
            )
            return _format_sql(sql_str)
        else:
            raise ValueError(f"Unsupported aggregation level: {aggregation_level}")

    else:
        sql_str = get_materialization_query(
            feature_view=feature_view,
            time_limits=pendulum.period(feature_start_time, feature_end_time),
            source=source,
        )
        return _format_sql(sql_str)


def get_materialization_query(
    feature_view: FeatureViewProto,
    # start is inclusive and end is exclusive
    time_limits: pendulum.Period,
    # If source is not provided, the query will use the registered Snowflake view for the FeatureView as the source.
    source: str = None,
):
    """Returns a SQL query for time-limited materialization.

    Does not include a terminating `;` or any COPY or INSERT statements."""
    if source is None:
        source = feature_view.snowflake_data.snowflake_view_name
    if feature_view.HasField("temporal_aggregate"):
        source = MATERIALIZATION_TILE_TEMPLATE.render(
            source=source,
            join_keys=list(feature_view.join_keys),
            aggregations=_get_feature_view_aggregations(feature_view),
            slide_interval=feature_view.temporal_aggregate.slide_interval,
            timestamp_key=feature_view.timestamp_key,
        )
    return _format_sql(
        MATERIALIZATION_TEMPLATE.render(
            source=source,
            materialization_schema=feature_view.schemas.materialization_schema,
            timestamp_key=feature_view.timestamp_key,
            start_time=time_limits.start,
            end_time=time_limits.end,
            cast_for_copy=True,
        )
    )


def get_materialization_copy_sql(
    feature_view: FeatureViewProto,
    # start is inclusive and end is exclusive
    time_limits: pendulum.Period,
    destination: str,
    storage_integration: Optional[str],
):
    """Returns a SQL query for a COPY INTO an external stage for materialization.

    Does not include a terminating `;`."""
    query = get_materialization_query(feature_view=feature_view, time_limits=time_limits)
    return _format_sql(
        ONLINE_STORE_COPIER_TEMPLATE.render(
            source=query,
            destination=destination,
            storage_integration=storage_integration,
        )
    )


def get_features_sql_str_for_spine(
    feature_set_config: FeatureSetConfig,
    timestamp_key: str,
    spine_sql: str = None,
    include_feature_view_timestamp_columns: bool = False,
) -> str:
    """
    Get a SQL string to fetch features given the spine and feature set.
    spine_sql and spine_table_name cannot be both empty.

    :param feature_set_config: FeatureSetConfig for the features.
    :param timestamp_key: Name of the time column in the spine.
    :param spine_sql: SQL str to get the spine.
    :param include_feature_view_timestamp_columns: (Optional) Include timestamp columns for every individual feature definitions.
    :return: A SQL string that can be used to fetch features.
    """
    if include_feature_view_timestamp_columns:
        # TODO(TEC-7238): Implement this
        raise TectonSnowflakeNotImplementedError(
            "include_feature_view_timestamp_columns is not implemented for Snowflake"
        )

    feature_set_items = feature_set_config._get_feature_definitions_and_join_configs()
    input_items = []
    for item in feature_set_items:
        fd = item.feature_definition
        feature_view = fd.fv
        join_keys = {key: value for key, value in item.join_keys}
        features = [
            col_name
            for col_name in fd.view_schema.column_names()
            if col_name not in (list(join_keys.keys()) + [fd.timestamp_key])
        ]
        if len(fd.online_serving_index.join_keys) != len(fd.join_keys):
            raise ValueError("SQL string does not support wildcard")
        sql_str = TIME_LIMIT_TEMPLATE.render(
            source=pipeline_to_sql_string(
                pipeline=fd.pipeline,
                data_sources=fd.data_sources,
                transformations=fd.transformations,
            ),
            timestamp_key=fd.timestamp_key,
            # Apply time limit from feature_start_time
            start_time=fd.start_timestamp,
        )
        input_items.append(
            _FeatureSetItemInput(
                name=fd.name,
                timestamp_key=fd.timestamp_key,
                join_keys=join_keys,
                features=features,
                sql=sql_str,
                aggregation=(feature_view.temporal_aggregate if feature_view.HasField("temporal_aggregate") else None),
                ttl_seconds=(int(fd.serving_ttl.total_seconds()) if fd.is_temporal else None),
            )
        )
    return _format_sql(
        HISTORICAL_FEATURES_TEMPLATE.render(
            feature_set_items=input_items,
            spine_timestamp_key=timestamp_key,
            spine_sql=spine_sql,
            include_feature_view_timestamp_columns=include_feature_view_timestamp_columns,
        )
    )


def _get_feature_view_aggregations(feature_view: FeatureViewProto) -> Dict[str, Set[str]]:
    aggregations = defaultdict(set)
    for feature in feature_view.temporal_aggregate.features:
        aggregate_function = AGGREGATION_PLANS[feature.function]
        if not aggregate_function:
            raise TectonSnowflakeNotImplementedError(
                f"Unsupported aggregation function {feature.function} in snowflake pipeline"
            )
        aggregations[feature.input_feature_name].update(aggregate_function)

    # Need to order the functions for deterministic results.
    for key, value in aggregations.items():
        aggregations[key] = sorted(value)

    return aggregations
