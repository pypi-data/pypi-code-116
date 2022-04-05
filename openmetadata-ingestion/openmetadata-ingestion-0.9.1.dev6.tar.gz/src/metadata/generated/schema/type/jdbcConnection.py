# generated by datamodel-codegen:
#   filename:  schema/type/jdbcConnection.json
#   timestamp: 2022-04-05T06:49:57+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class DriverClass(BaseModel):
    __root__: str = Field(..., description='Type used for JDBC driver class.')


class ConnectionUrl(BaseModel):
    __root__: str = Field(
        ...,
        description='Type used for JDBC connection URL of format `url_scheme://<username>:<password>@<host>:<port>/<db_name>`.',
    )


class JdbcInfo(BaseModel):
    class Config:
        extra = Extra.forbid

    driverClass: DriverClass
    connectionUrl: ConnectionUrl


class JdbcConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    driverClass: DriverClass = Field(..., description='JDBC driver class.')
    connectionUrl: ConnectionUrl = Field(..., description='JDBC connection URL.')
    userName: str = Field(..., description='Login user name.')
    password: str = Field(..., description='Login password.')
