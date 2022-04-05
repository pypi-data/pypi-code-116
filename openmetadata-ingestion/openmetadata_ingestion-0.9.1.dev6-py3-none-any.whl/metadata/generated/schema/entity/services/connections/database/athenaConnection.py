# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/database/athenaConnection.json
#   timestamp: 2022-04-05T04:21:49+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field, SecretStr

from . import connectionBasicType


class SupportedPipelineType22(Enum):
    Metadata = 'Metadata'


class AthenaType(Enum):
    Athena = 'Athena'


class AthenaScheme(Enum):
    awsathena_rest = 'awsathena+rest'


class AthenaConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    serviceType: Optional[AthenaType] = Field('Athena', description='Service Type')
    scheme: Optional[AthenaScheme] = Field(
        'awsathena+rest', description='SQLAlchemy driver scheme options.'
    )
    username: Optional[str] = Field(
        None,
        description='username to connect  to the Athena. This user should have privileges to read all the metadata in Athena.',
    )
    password: Optional[SecretStr] = Field(
        None, description='password to connect  to the Athena.'
    )
    hostPort: Optional[str] = Field(None, description='Host and port of the Athena')
    database: Optional[str] = Field(
        None,
        description='Database of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single database. When left blank , OpenMetadata Ingestion attempts to scan all the databases in Athena.',
    )
    awsRegion: Optional[str] = Field(None, description='AWS Athena AWS Region. ')
    s3StagingDir: Optional[str] = Field(None, description='S3 Staging Directory.')
    workgroup: Optional[str] = Field(None, description='Athena workgroup.')
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = None
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = None
    supportedPipelineTypes: Optional[List[SupportedPipelineType22]] = Field(
        ['Metadata'], description='Supported Metadata Extraction Pipelines.'
    )
