# generated by datamodel-codegen:
#   filename:  schema/entity/services/messagingService.json
#   timestamp: 2022-04-05T06:49:57+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Extra, Field, constr

from ...type import basic, entityHistory, entityReference, schedule


class MessagingServiceType(Enum):
    Kafka = 'Kafka'
    Pulsar = 'Pulsar'


class Brokers(BaseModel):
    __root__: List[str] = Field(
        ...,
        description='Multiple bootstrap addresses for Kafka. Single proxy address for Pulsar.',
    )


class MessagingService(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier of this messaging service instance.'
    )
    name: constr(regex=r'^[^.]*$', min_length=1, max_length=128) = Field(
        ..., description='Name that identifies this messaging service.'
    )
    serviceType: MessagingServiceType = Field(
        ..., description='Type of messaging service such as Kafka or Pulsar...'
    )
    description: Optional[str] = Field(
        None, description='Description of a messaging service instance.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this messaging service. It could be title or label from the source services.',
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    brokers: Brokers = Field(
        ...,
        description='Multiple bootstrap addresses for Kafka. Single proxy address for Pulsar.',
    )
    schemaRegistry: Optional[AnyUrl] = Field(None, description='Schema registry URL.')
    ingestionSchedule: Optional[schedule.Schedule] = Field(
        None, description='Schedule for running metadata ingestion jobs.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this messaging service.'
    )
    href: Optional[basic.Href] = Field(
        None,
        description='Link to the resource corresponding to this messaging service.',
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
