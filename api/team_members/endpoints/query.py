import strawberry

from api.team_members.dependencies import get_team_member_service
from api.team_members.schemas import TeamMemberUpdateSchema, TeamMemberGetSchema


@strawberry.type
class TeamMemberQuery:
    @strawberry.field
    async def team_members(
        self,
        filters: TeamMemberUpdateSchema
    ) -> list[TeamMemberGetSchema]:
        return await get_team_member_service().get_all(filters)
