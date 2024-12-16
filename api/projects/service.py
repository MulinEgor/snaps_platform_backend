from strawberry.exceptions import GraphQLError

from api.projects.repository import ProjectRepository
from api.projects.types.response import ProjectGetSchema
from api.projects.types.request import ProjectSchema, ProjectOptionalSchema
from api.service import Service


class ProjectService(Service):
    def __init__(self, repository: ProjectRepository):
        super().__init__(self.__class__.__name__, repository)
        self.repository: ProjectRepository

    async def get(self, uuid: str) -> ProjectGetSchema | None:
        self.logger.info(f"Fetching project with uuid: {uuid}")
        project = await self.repository.get(uuid)
        if not project:
            self.handle_error(f"Project with uuid: {uuid} not found")
        self.logger.info(f"Project with uuid: {uuid} retrieved successfully")
        return project

    async def get_all(self, filters: ProjectOptionalSchema) -> list[ProjectGetSchema] | None:
        self.logger.info(f"Fetching all projects with filters: \n{
                         filters.to_dict()}")
        projects = await self.repository.get_all(filters)
        if not projects:
            self.handle_error("No projects found")
        self.logger.info(f"Retrieved {len(projects)} projects")
        return projects

    async def create(self, data: ProjectSchema) -> ProjectGetSchema | None:
        self.logger.info(f"Creating project with data: \n{data.__dict__}")
        project = await self.repository.create(data)
        if not project:
            self.handle_error("Failed to create project")
        self.logger.info(f"Project created successfully with uuid: {
                         project.uuid}")
        return project

    async def update(self, uuid: str, data: ProjectOptionalSchema) -> ProjectGetSchema | None:
        self.logger.info(f"Updating project with uuid: {
                         uuid} and data: \n{data.to_dict()}")
        await self.get(uuid)

        project = await self.repository.update(uuid, data)
        if not project:
            self.handle_error(f"Failed to update project with uuid: {uuid}")
        self.logger.info(f"Project with uuid: {uuid} updated successfully")
        return project

    async def delete(self, uuid: str) -> ProjectGetSchema | None:
        self.logger.info(f"Deleting project with uuid: {uuid}")
        await self.get(uuid)

        project = await self.repository.delete(uuid)
        if not project:
            self.handle_error(f"Failed to delete project with uuid: {uuid}")
        self.logger.info(f"Project with uuid: {uuid} deleted successfully")
        return project
