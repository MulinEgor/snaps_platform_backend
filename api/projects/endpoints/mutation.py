import strawberry

from api.projects.dependencies import get_project_service
from api.projects.schemas import ProjectGetSchema, ProjectUpdateSchema, ProjectCreateSchema


@strawberry.type
class ProjectMutation:
    @strawberry.mutation
    async def create(
        self,
        schema: ProjectCreateSchema
    ) -> ProjectGetSchema | None:
        return await get_project_service().create(schema)

    @strawberry.mutation
    async def update(
        self,
        uuid: str,
        schema: ProjectUpdateSchema
    ) -> ProjectGetSchema | None:
        return await get_project_service().update(uuid, schema)

    @strawberry.mutation
    async def delete(
        self,
        uuid: str
    ) -> ProjectGetSchema | None:
        return await get_project_service().delete(uuid)
