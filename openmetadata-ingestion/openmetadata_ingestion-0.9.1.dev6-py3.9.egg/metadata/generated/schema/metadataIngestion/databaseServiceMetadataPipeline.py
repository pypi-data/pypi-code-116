# generated by datamodel-codegen:
#   filename:  schema/metadataIngestion/databaseServiceMetadataPipeline.json
#   timestamp: 2022-04-05T04:21:49+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ..type import filterPattern


class DatabaseServiceMetadataPipeline(BaseModel):
    class Config:
        extra = Extra.forbid

    markDeletedTables: Optional[bool] = Field(
        'true',
        description='Optional configuration to soft delete tables in OpenMetadata if the source tables are deleted.',
    )
    includeViews: Optional[bool] = Field(
        'true',
        description='Optional configuration to turn off fetching metadata for views.',
    )
    generateSampleData: Optional[bool] = Field(
        'true',
        description='Option to turn on/off generating sample data during metadata extraction.',
    )
    sampleDataQuery: Optional[str] = Field(
        'select * from {}.{} limit 50', description='Sample data extraction query.'
    )
    enableDataProfiler: Optional[bool] = Field(
        'false',
        description='Run data profiler as part of this metadata ingestion to get table profile data.',
    )
    schemaFilterPattern: Optional[filterPattern.FilterPattern] = Field(
        None,
        description='Regex to only fetch tables or databases that matches the pattern.',
    )
    tableFilterPattern: Optional[filterPattern.FilterPattern] = Field(
        None, description='Regex exclude tables or databases that matches the pattern.'
    )
    dbtCatalogFilePath: Optional[str] = Field(
        None,
        description='DBT catalog file to extract dbt models with their column schemas.',
    )
    dbtManifestFilePath: Optional[str] = Field(
        None,
        description='DBT manifest file path to extract dbt models and associate with tables.',
    )
