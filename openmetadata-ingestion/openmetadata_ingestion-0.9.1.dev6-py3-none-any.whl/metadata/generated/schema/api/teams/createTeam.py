# generated by datamodel-codegen:
#   filename:  schema/api/teams/createTeam.json
#   timestamp: 2022-04-05T06:49:57+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...entity.teams import team
from ...type import basic, profile


class CreateTeamRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: team.TeamName
    displayName: Optional[str] = Field(
        None,
        description="Optional name used for display purposes. Example 'Marketing Team'.",
    )
    description: Optional[str] = Field(
        None, description='Optional description of the team.'
    )
    profile: Optional[profile.Profile] = Field(
        None, description='Optional team profile information.'
    )
    users: Optional[List[basic.Uuid]] = Field(
        None, description='Optional IDs of users that are part of the team.'
    )
    defaultRoles: Optional[List[basic.Uuid]] = Field(
        None,
        description='Roles to be assigned to all users that are part of this team.',
    )
