import strawberry

from api.projects.dependencies import get_project_service
from api.projects.types.request import ProjectSchema, ProjectOptionalSchema
from api.projects.types.response import ProjectGetSchema


@strawberry.type
class ProjectMutation:
    @strawberry.mutation
    async def create(
        self,
        schema: ProjectSchema
    ) -> ProjectGetSchema | None:
        return await get_project_service().create(schema)

    @strawberry.mutation
    async def update(
        self,
        uuid: str,
        schema: ProjectOptionalSchema
    ) -> ProjectGetSchema | None:
        return await get_project_service().update(uuid, schema)

    @strawberry.mutation
    async def delete(
        self,
        uuid: str
    ) -> ProjectGetSchema | None:
        return await get_project_service().delete(uuid)
