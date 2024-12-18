from prisma.models import TeamMember

from api.team_members.types.request import TeamMemberSchema, TeamMemberOptionalSchema
from api.repository import Repository


class TeamMemberRepository(Repository):
    def __init__(self):
        super().__init__('teammember')

    async def get(self, uuid: str) -> TeamMember | None:
        return await super().get(uuid)

    async def get_all(self, filters: TeamMemberOptionalSchema) -> list[TeamMember] | None:
        return await super().get_all(filters.to_dict())

    async def create(self, data: TeamMemberSchema) -> TeamMember:
        return await super().create(data.__dict__)

    async def update(self, uuid: str, data: TeamMemberOptionalSchema) -> TeamMember:
        return await super().update(uuid, data.to_dict())

    async def delete(self, uuid: str) -> TeamMember:
        return await super().delete(uuid)
