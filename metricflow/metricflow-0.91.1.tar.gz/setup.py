# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['metricflow',
 'metricflow.cli',
 'metricflow.configuration',
 'metricflow.constraints',
 'metricflow.dag',
 'metricflow.dataflow',
 'metricflow.dataflow.builder',
 'metricflow.dataset',
 'metricflow.engine',
 'metricflow.errors',
 'metricflow.execution',
 'metricflow.model',
 'metricflow.model.objects',
 'metricflow.model.objects.constraints',
 'metricflow.model.objects.elements',
 'metricflow.model.parsing',
 'metricflow.model.semantics',
 'metricflow.model.transformations',
 'metricflow.model.validations',
 'metricflow.naming',
 'metricflow.plan_conversion',
 'metricflow.protocols',
 'metricflow.query',
 'metricflow.sql',
 'metricflow.sql.optimizer',
 'metricflow.sql.render',
 'metricflow.sql_clients',
 'metricflow.test',
 'metricflow.test.cli',
 'metricflow.test.constraints',
 'metricflow.test.dataflow',
 'metricflow.test.dataflow.builder',
 'metricflow.test.dataset',
 'metricflow.test.execution',
 'metricflow.test.fixtures',
 'metricflow.test.integration',
 'metricflow.test.model',
 'metricflow.test.model.semantics',
 'metricflow.test.model.validations',
 'metricflow.test.plan_conversion',
 'metricflow.test.plan_conversion.instance_converters',
 'metricflow.test.query',
 'metricflow.test.sql',
 'metricflow.test.sql.optimizer',
 'metricflow.test.sql_clients',
 'metricflow.test.time',
 'metricflow.time']

package_data = \
{'': ['*'],
 'metricflow.test': ['snapshots/test_column_pruner.py/SqlQueryPlan/*',
                     'snapshots/test_convert_data_source.py/SqlQueryPlan/BigQuerySqlClient/*',
                     'snapshots/test_convert_data_source.py/SqlQueryPlan/RedshiftSqlClient/*',
                     'snapshots/test_convert_data_source.py/SqlQueryPlan/SnowflakeSqlClient/*',
                     'snapshots/test_convert_data_source.py/SqlQueryPlan/SqliteSqlClient/*',
                     'snapshots/test_dataflow_plan_builder.py/DataflowPlan/*',
                     'snapshots/test_dataflow_to_execution.py/ExecutionPlan/BigQuerySqlClient/*',
                     'snapshots/test_dataflow_to_execution.py/ExecutionPlan/RedshiftSqlClient/*',
                     'snapshots/test_dataflow_to_execution.py/ExecutionPlan/SnowflakeSqlClient/*',
                     'snapshots/test_dataflow_to_execution.py/ExecutionPlan/SqliteSqlClient/*',
                     'snapshots/test_dataflow_to_sql_plan.py/DataflowPlan/*',
                     'snapshots/test_dataflow_to_sql_plan.py/SqlQueryPlan/*',
                     'snapshots/test_dataflow_to_sql_plan.py/SqlQueryPlan/BigQuerySqlClient/*',
                     'snapshots/test_dataflow_to_sql_plan.py/SqlQueryPlan/RedshiftSqlClient/*',
                     'snapshots/test_dataflow_to_sql_plan.py/SqlQueryPlan/SnowflakeSqlClient/*',
                     'snapshots/test_dataflow_to_sql_plan.py/SqlQueryPlan/SqliteSqlClient/*',
                     'snapshots/test_engine_specific_rendering.py/SqlQueryPlan/BigQuerySqlClient/*',
                     'snapshots/test_engine_specific_rendering.py/SqlQueryPlan/RedshiftSqlClient/*',
                     'snapshots/test_engine_specific_rendering.py/SqlQueryPlan/SnowflakeSqlClient/*',
                     'snapshots/test_engine_specific_rendering.py/SqlQueryPlan/SqliteSqlClient/*',
                     'snapshots/test_rendered_query.py/MetricFlowExplainResult/BigQuerySqlClient/*',
                     'snapshots/test_rendered_query.py/MetricFlowExplainResult/RedshiftSqlClient/*',
                     'snapshots/test_rendered_query.py/MetricFlowExplainResult/SnowflakeSqlClient/*',
                     'snapshots/test_rendered_query.py/MetricFlowExplainResult/SqliteSqlClient/*',
                     'snapshots/test_rewriting_sub_query_reducer.py/SqlQueryPlan/*',
                     'snapshots/test_sql_plan_render.py/SqlQueryPlan/BigQuerySqlClient/*',
                     'snapshots/test_sql_plan_render.py/SqlQueryPlan/RedshiftSqlClient/*',
                     'snapshots/test_sql_plan_render.py/SqlQueryPlan/SnowflakeSqlClient/*',
                     'snapshots/test_sql_plan_render.py/SqlQueryPlan/SqliteSqlClient/*',
                     'snapshots/test_sub_query_reducer.py/SqlQueryPlan/*',
                     'snapshots/test_table_alias_simplifier.py/SqlQueryPlan/*'],
 'metricflow.test.fixtures': ['model_yamls/composite_identifier_model/*',
                              'model_yamls/extended_date_model/data_sources/*',
                              'model_yamls/join_types_model/*',
                              'model_yamls/multi_hop_join_model/partitioned_data_sources/*',
                              'model_yamls/multi_hop_join_model/unpartitioned_data_sources/*',
                              'model_yamls/non_ds_model/*',
                              'model_yamls/simple_model/*',
                              'model_yamls/simple_model/data_sources/*'],
 'metricflow.test.integration': ['test_cases/*']}

install_requires = \
['Jinja2==2.11.3',
 'MarkupSafe==2.0.1',
 'PyYAML>=5.4.1,<6.0.0',
 'SQLAlchemy>=1.4.27,<2.0.0',
 'ciso8601>=2.2.0,<3.0.0',
 'click>=7.1.2,<8.0.0',
 'croniter>=1.3.4,<2.0.0',
 'ddtrace>=0.60.0,<0.61.0',
 'fuzzywuzzy>=0.18.0,<0.19.0',
 'google-cloud-bigquery==2.34.2',
 'graphviz==0.18.2',
 'halo>=0.0.31,<0.0.32',
 'jsonschema==3.2.0',
 'more-itertools==8.10.0',
 'moz-sql-parser>=4.40.21126,<5.0.0',
 'mysqlclient>=2.1.0,<3.0.0',
 'numpy==1.22.0',
 'pandas==1.2.4',
 'psycopg2>=2.9.3,<3.0.0',
 'pycron>=3.0.0,<4.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'python-Levenshtein>=0.12.2,<0.13.0',
 'python-dateutil==2.8.2',
 'requests>=2.27.1,<3.0.0',
 'snowflake-connector-python>=2.7.6,<3.0.0',
 'snowflake-sqlalchemy==1.2.3',
 'sqlalchemy-bigquery>=1.4.3,<2.0.0',
 'sqlalchemy-redshift==0.8.1',
 'sqlalchemy2-stubs>=0.0.2-alpha.21,<0.0.3',
 'tabulate==0.8.9',
 'update-checker>=0.18.0,<0.19.0']

entry_points = \
{'console_scripts': ['mf = metricflow.cli.main:cli']}

setup_kwargs = {
    'name': 'metricflow',
    'version': '0.91.1',
    'description': '',
    'long_description': None,
    'author': 'Transform',
    'author_email': 'hello@transformdata.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
