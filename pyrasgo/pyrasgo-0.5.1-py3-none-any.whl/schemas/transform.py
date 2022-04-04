from datetime import datetime
from typing import Dict, List, Optional, Any

from pydantic import BaseModel, Field


class TransformArgumentCreate(BaseModel):
    name: str
    description: str
    type: str
    is_optional: Optional[bool]


class TransformArgument(TransformArgumentCreate):
    pass


class TransformCreate(BaseModel):
    name: Optional[str]
    type: Optional[str]
    sourceCode: str
    description: Optional[str]
    arguments: Optional[List[TransformArgumentCreate]]
    tags: Optional[List[str]]
    context: Optional[Dict[str, Any]]


class TransformUpdate(BaseModel):
    """
    Contract for updating a Transform
    """
    name: Optional[str]
    type: Optional[str]
    description: Optional[str]
    sourceCode: Optional[str]
    arguments: Optional[List[TransformArgumentCreate]]
    tags: Optional[List[str]]
    context: Optional[Dict[str, Any]]


class Transform(TransformCreate):
    id: Optional[int]
    arguments: Optional[List[TransformArgument]]


class TransformExecute(BaseModel):
    transform_args: Dict[str, Any] = Field(alias='transformArgs')
    transform_id: int = Field(alias='transformId')
    class Config:
        allow_population_by_field_name = True
