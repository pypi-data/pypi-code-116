# generated by datamodel-codegen:
#   filename:  schema/tests/table/tableRowCountToEqual.json
#   timestamp: 2022-04-05T06:49:57+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class TableRowCountToEqual(BaseModel):
    class Config:
        extra = Extra.forbid

    value: int = Field(..., description='Expected number of rows {value}')
