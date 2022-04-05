# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/database/azureSQLConnection.json
#   timestamp: 2022-04-05T04:21:49+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field, SecretStr

from . import connectionBasicType


class SupportedPipelineType13(Enum):
    Metadata = 'Metadata'


class AzureSQLType(Enum):
    AzureSQL = 'AzureSQL'


class AzureSQLScheme(Enum):
    mssql_pyodbc = 'mssql+pyodbc'


class AzureSQLConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[AzureSQLType] = Field('AzureSQL', description='Service Type')
    scheme: Optional[AzureSQLScheme] = Field(
        'mssql+pyodbc', description='SQLAlchemy driver scheme options.'
    )
    username: Optional[str] = Field(
        None,
        description='username to connect  to the Athena. This user should have privileges to read all the metadata in Azure SQL.',
    )
    password: Optional[SecretStr] = Field(
        None, description='password to connect  to the Athena.'
    )
    hostPort: Optional[str] = Field(None, description='Host and port of the Athena')
    database: Optional[str] = Field(
        None,
        description='Database of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single database. When left blank , OpenMetadata Ingestion attempts to scan all the databases in Azure SQL.',
    )
    driver: Optional[str] = Field(
        '{ODBC Driver 17 for SQL Server}', description='SQLAlchemy driver for Azure SQL'
    )
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = None
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = None
    supportedPipelineTypes: Optional[List[SupportedPipelineType13]] = Field(
        ['Metadata'], description='Supported Metadata Extraction Pipelines.'
    )
