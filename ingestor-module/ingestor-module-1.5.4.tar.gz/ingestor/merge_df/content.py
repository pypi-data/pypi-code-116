from typing import Tuple

import pandas as pd
from graphdb.connection import GraphDbConnection
from pandas import DataFrame

from ingestor.common.constants import CONTENT_ID
from ingestor.content_profile.network.content import ContentNetworkGenerator
from ingestor.merge_df.common import CommonUtils


class FinalDfController:

    @staticmethod
    def build_content_profile_final_df(df_content, df_country, df_actor, df_tag, df_homepage, df_content_core,
                                       df_content_bundle_having_content, df_package_having_content_bundle,
                                       df_product_having_package) -> DataFrame:
        content_df = DataFrame()
        result_not_in_df = DataFrame()
        if not pd.isna(df_content[CONTENT_ID][0]):
            content_df, result_not_in_df = CommonUtils.fetch_prepare_content_id(content_df, df_content,
                                                                                result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_created_on(content_df, df_content,
                                                                                result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_title(content_df, df_content, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_synopsis(content_df, df_content, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_synopsis_en(content_df, df_content,
                                                                                 result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_type(content_df, df_content, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_status(content_df, df_content, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_year(content_df, df_content, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_rating(content_df, df_content, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_is_free(content_df, df_content, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_is_original(content_df, df_content,
                                                                                 result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_is_exclusive(content_df, df_content,
                                                                                  result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_is_branded(content_df, df_content,
                                                                                result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_is_geo_block(content_df, df_content,
                                                                                  result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_duration(content_df, df_content, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_start_date(content_df, df_content,
                                                                                result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_end_date(content_df, df_content, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_modified_on(content_df, df_content,
                                                                                 result_not_in_df)

            content_df, result_not_in_df = CommonUtils.fetch_prepare_country(content_df, df_content, df_country,
                                                                             result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_category(content_df, df_content,
                                                                              result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_subcategory(content_df, df_content,
                                                                                 result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_actors(content_df, df_content,
                                                                            df_actor, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_tags(content_df, df_content,
                                                                          df_tag, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_homepages(content_df, df_content,
                                                                               df_homepage, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_content_cores(content_df, df_content,
                                                                                   df_content_core, result_not_in_df)
            content_df, result_not_in_df = CommonUtils.fetch_prepare_product_package(content_df, df_content,
                                                                                     df_content_bundle_having_content,
                                                                                     df_package_having_content_bundle,
                                                                                     df_product_having_package,
                                                                                     result_not_in_df)

        return content_df, result_not_in_df

    @staticmethod
    def get_final_df_content_profile(
            df_content,
            df_country,
            df_actor,
            df_tag, df_homepage,
            df_content_core,
            df_product_having_package,
            df_content_having_bundle,
            df_package_having_content_bundle,
            connection_uri,
            connection: GraphDbConnection = None
    ) -> Tuple[DataFrame, DataFrame]:
        """Calculate final dataframe for content profile
        :param connection_uri:
        :param df: dataframe that get for content csv file
        :param df_content: dataframe object for country value
        :param df_actor: dataframe object for actor value
        :param df_tag: dataframe object for tag value
        :param df_homepage: dataframe object for homepage value
        :param df_content_core: dataframe object for content core value
        :param df_product_having_package: dataframe object for product having package value
        :param df_content_having_bundle: dataframe object for content having bundle value
        :param df_package_having_content_bundle: dataframe object for package having content bundle value
        :param connection: object connection to gremlin or AWS Neptune
        :return: tuple dataframe
        """
        if connection is not None:
            cls = ContentNetworkGenerator.from_connection_class(connection)
        else:
            cls = ContentNetworkGenerator.from_connection_uri(connection_uri)
        final_df_content_profile = DataFrame()
        result_not_correct_df = DataFrame()

        for row, val in df_content.iterrows():
            print("dumping content profile for {0}".format(val))
            df_new = DataFrame()
            values_to_add = val.to_dict()
            row_to_add = pd.Series(values_to_add)
            new_df = pd.concat([df_new, row_to_add], axis=1).T
            result_df, result_not_df = FinalDfController.build_content_profile_final_df(
                new_df, df_country, df_actor, df_tag,
                df_homepage,
                df_content_core,
                df_content_having_bundle,
                df_package_having_content_bundle,
                df_product_having_package)

            cls.content_creator_updater_network(payload=result_df)
            print("Successfully dumped content profile for {0}".format(val))

            final_df_content_profile = pd.concat([final_df_content_profile, result_df], axis=0)
            result_not_correct_df = pd.concat([result_not_correct_df, result_not_df], axis=0)

        return final_df_content_profile, result_not_correct_df
