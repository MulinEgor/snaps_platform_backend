import strawberry

from api.team_members.types.request import TeamMemberSchema


@strawberry.type
class TeamMemberGetSchema(TeamMemberSchema):
    uuid: str
