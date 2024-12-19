from strawberry.exceptions import GraphQLError

from api.projects.repository import ProjectRepository
from api.projects.types.response import ProjectGetSchema
from api.projects.types.request import ProjectSchema, ProjectOptionalSchema
from api.service import Service


class ProjectService(Service):
    def __init__(self, repository: ProjectRepository):
        super().__init__(self.__class__.__name__, repository)
        self._repository: ProjectRepository

    async def get(self, uuid: str) -> ProjectGetSchema | None:
        self._logger.info(f"Fetching data with uuid: {uuid}")
        project = await self._repository.get(uuid)
        if not project:
            self._handle_error(f"Data with uuid: {uuid} not found")
        self._logger.info(f"Data with uuid: {uuid} retrieved successfully")
        return project

    async def get_all(self, filters: ProjectOptionalSchema) -> list[ProjectGetSchema] | None:
        self._logger.info(f"Fetching all data with filters: \n{
            filters.to_dict()}")
        projects = await self._repository.get_all(filters)
        if not projects:
            self._handle_error("No data found")
        self._logger.info(f"Retrieved data with size {len(projects)}")
        return projects

    async def create(self, data: ProjectSchema) -> ProjectGetSchema | None:
        self._logger.info(f"Creating data: \n{data.__dict__}")
        project = await self._repository.create(data)
        if not project:
            self._handle_error("Failed to create")
        self._logger.info(f"Data created successfully with uuid: {
            project.uuid}")
        return project

    async def update(self, uuid: str, data: ProjectOptionalSchema) -> ProjectGetSchema | None:
        self._logger.info(f"Updating data with uuid: {
            uuid} and data: \n{data.to_dict()}")
        await self.get(uuid)

        project = await self._repository.update(uuid, data)
        if not project:
            self._handle_error(f"Failed to update data with uuid: {uuid}")
        self._logger.info(f"Data with uuid: {uuid} updated successfully")
        return project

    async def delete(self, uuid: str) -> ProjectGetSchema | None:
        self._logger.info(f"Deleting data with uuid: {uuid}")
        await self.get(uuid)

        project = await self._repository.delete(uuid)
        if not project:
            self._handle_error(f"Failed to delete data with uuid: {uuid}")
        self._logger.info(f"Data with uuid: {uuid} deleted successfully")
        return project
