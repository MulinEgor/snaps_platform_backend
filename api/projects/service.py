from api.projects.repository import ProjectRepository
from api.projects.schemas import ProjectGetSchema, ProjectUpdateSchema, ProjectCreateSchema
from api.service import Service


class ProjectService(Service):
    def __init__(self, repository: ProjectRepository):
        super().__init__(self.__class__.__name__, repository)
        self._repository: ProjectRepository

    async def get(self, uuid: str) -> ProjectGetSchema | None:
        return await super().get(uuid)

    async def get_all(self, filters: ProjectUpdateSchema) -> list[ProjectGetSchema] | None:
        return await super().get_all(filters)

    async def create(self, data: ProjectCreateSchema) -> ProjectGetSchema | None:
        return await super().create(data)

    async def update(self, uuid: str, data: ProjectUpdateSchema) -> ProjectGetSchema | None:
        return await super().update(uuid, data)

    async def delete(self, uuid: str) -> ProjectGetSchema | None:
        return await super().delete(uuid)
