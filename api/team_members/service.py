from api.team_members.repository import TeamMemberRepository
from api.team_members.types.response import TeamMemberGetSchema
from api.team_members.types.request import TeamMemberSchema, TeamMemberOptionalSchema
from api.service import Service


class TeamMemberService(Service):
    def __init__(self, repository: TeamMemberRepository):
        super().__init__(self.__class__.__name__, repository)
        self._repository: TeamMemberRepository

    async def get(self, uuid: str) -> TeamMemberGetSchema | None:
        self._logger.info(f"Fetching data with uuid: {uuid}")
        team_member = await self._repository.get(uuid)
        if not team_member:
            self._handle_error(f"Data with uuid: {uuid} not found")
        self._logger.info(f"Data with uuid: {uuid} retrieved successfully")
        return team_member

    async def get_all(self, filters: TeamMemberOptionalSchema) -> list[TeamMemberGetSchema] | None:
        self._logger.info(f"Fetching all data with filters: \n{
            filters.to_dict()}")
        team_members = await self._repository.get_all(filters)
        if not team_members:
            self._handle_error("No data found")
        self._logger.info(f"Retrieved data with size {len(team_members)}")
        return team_members

    async def create(self, data: TeamMemberSchema) -> TeamMemberGetSchema | None:
        self._logger.info(f"Creating data: \n{data.__dict__()}")
        team_member = await self._repository.create(data)
        if not team_member:
            self._handle_error("Failed to create")
        self._logger.info(f"Data created successfully with uuid: {
            team_member.uuid}")
        return team_member

    async def update(self, uuid: str, data: TeamMemberOptionalSchema) -> TeamMemberGetSchema | None:
        self._logger.info(f"Updating data with uuid: {
            uuid} and data: \n{data.to_dict()}")
        await self.get(uuid)

        team_member = await self._repository.update(uuid, data)
        if not team_member:
            self._handle_error(f"Failed to update data with uuid: {uuid}")
        self._logger.info(f"Data with uuid: {uuid} updated successfully")
        return team_member

    async def delete(self, uuid: str) -> TeamMemberGetSchema | None:
        self._logger.info(f"Deleting data with uuid: {uuid}")
        await self.get(uuid)

        team_member = await self._repository.delete(uuid)
        if not team_member:
            self._handle_error(f"Failed to delete data with uuid: {uuid}")
        self._logger.info(f"Data with uuid: {uuid} deleted successfully")
        return team_member
