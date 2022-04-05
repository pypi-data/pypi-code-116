# generated by datamodel-codegen:
#   filename:  schema/tests/table/tableColumnCountToEqual.json
#   timestamp: 2022-04-05T06:49:57+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class TableColumnCountToEqual(BaseModel):
    class Config:
        extra = Extra.forbid

    columnCount: int = Field(
        ..., description='Expected number of columns to equal to a {value}'
    )
