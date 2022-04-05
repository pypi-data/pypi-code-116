# generated by datamodel-codegen:
#   filename:  schema/api/data/createDatabase.json
#   timestamp: 2022-04-05T06:49:57+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...entity.data import database
from ...type import entityReference


class CreateDatabaseRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: database.DatabaseName = Field(
        ..., description='Name that identifies this database instance uniquely.'
    )
    description: Optional[str] = Field(
        None,
        description='Description of the database instance. What it has and how to use it.',
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this database'
    )
    service: entityReference.EntityReference = Field(
        ..., description='Link to the database service where this database is hosted in'
    )
