import strawberry

from api.auth.utils import requires_admin
from api.projects.dependencies import get_project_service
from api.projects.schemas import ProjectGetSchema, ProjectUpdateSchema, ProjectCreateSchema


@strawberry.type
class ProjectMutation:
    @strawberry.mutation
    @requires_admin
    async def create(
        self,
        info: strawberry.Info,
        schema: ProjectCreateSchema
    ) -> ProjectGetSchema | None:
        return await get_project_service().create(schema)

    @strawberry.mutation
    @requires_admin
    async def update(
        self,
        info: strawberry.Info,
        uuid: str,
        schema: ProjectUpdateSchema
    ) -> ProjectGetSchema | None:
        return await get_project_service().update(uuid, schema)

    @strawberry.mutation
    @requires_admin
    async def delete(
        self,
        info: strawberry.Info,
        uuid: str
    ) -> ProjectGetSchema | None:
        return await get_project_service().delete(uuid)
