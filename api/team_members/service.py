from api.team_members.repository import TeamMemberRepository
from api.team_members.schemas import TeamMemberCreateSchema, TeamMemberUpdateSchema, TeamMemberGetSchema
from api.service import Service


class TeamMemberService(Service):
    def __init__(self, repository: TeamMemberRepository):
        super().__init__(self.__class__.__name__, repository)
        self._repository: TeamMemberRepository

    async def get(self, uuid: str) -> TeamMemberGetSchema | None:
        return super().get(uuid)

    async def get_all(self, filters: TeamMemberUpdateSchema) -> list[TeamMemberGetSchema] | None:
        return super().get_all(filters)

    async def create(self, data: TeamMemberCreateSchema) -> TeamMemberGetSchema | None:
        return super().create(data)

    async def update(self, uuid: str, data: TeamMemberUpdateSchema) -> TeamMemberGetSchema | None:
        return super().update(uuid, data)

    async def delete(self, uuid: str) -> TeamMemberGetSchema | None:
        return super().delete(uuid)
