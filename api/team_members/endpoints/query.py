import strawberry

from api.team_members.dependencies import get_team_member_service
from api.team_members.types.request import TeamMemberOptionalSchema
from api.team_members.types.response import TeamMemberGetSchema


@strawberry.type
class TeamMemberQuery:
    @strawberry.field
    async def team_members(
        self,
        filters: TeamMemberOptionalSchema
    ) -> list[TeamMemberGetSchema]:
        return await get_team_member_service().get_all(filters)
