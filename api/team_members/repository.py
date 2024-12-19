from prisma.models import TeamMember

from api.team_members.schemas import TeamMemberCreateSchema, TeamMemberUpdateSchema
from api.repository import Repository


class TeamMemberRepository(Repository):
    def __init__(self):
        super().__init__('teammember')

    async def get(self, uuid: str) -> TeamMember | None:
        return await super().get(uuid)

    async def get_all(self, filters: TeamMemberUpdateSchema) -> list[TeamMember] | None:
        return await super().get_all(filters.to_dict())

    async def create(self, data: TeamMemberCreateSchema) -> TeamMember:
        return await super().create(data.__dict__)

    async def update(self, uuid: str, data: TeamMemberUpdateSchema) -> TeamMember:
        return await super().update(uuid, data.to_dict())

    async def delete(self, uuid: str) -> TeamMember:
        return await super().delete(uuid)
