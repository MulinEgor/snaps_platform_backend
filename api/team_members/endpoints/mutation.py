import strawberry

from api.team_members.dependencies import get_team_member_service
from api.team_members.schemas import TeamMemberCreateSchema, TeamMemberUpdateSchema, TeamMemberGetSchema


@strawberry.type
class TeamMemberMutation:
    @strawberry.mutation
    async def create(
        self,
        schema: TeamMemberCreateSchema
    ) -> TeamMemberGetSchema | None:
        return await get_team_member_service().create(schema)

    @strawberry.mutation
    async def update(
        self,
        uuid: str,
        schema: TeamMemberUpdateSchema
    ) -> TeamMemberGetSchema | None:
        return await get_team_member_service().update(uuid, schema)

    @strawberry.mutation
    async def delete(
        self,
        uuid: str
    ) -> TeamMemberGetSchema | None:
        return await get_team_member_service().delete(uuid)
