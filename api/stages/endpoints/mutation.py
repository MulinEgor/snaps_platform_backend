import strawberry

from api.auth.utils import requires_admin
from api.stages.dependencies import get_stage_service
from api.stages.schemas import StageCreateSchema, StageUpdateSchema, StageGetSchema


@strawberry.type
class StageMutation:
    @strawberry.mutation
    @requires_admin
    async def create(
        self,
        info: strawberry.Info,
        schema: StageCreateSchema
    ) -> StageGetSchema | None:
        return await get_stage_service().create(schema)

    @strawberry.mutation
    @requires_admin
    async def update(
        self,
        info: strawberry.Info,
        uuid: str,
        schema: StageUpdateSchema
    ) -> StageGetSchema | None:
        return await get_stage_service().update(uuid, schema)

    @strawberry.mutation
    @requires_admin
    async def delete(
        self,
        info: strawberry.Info,
        uuid: str
    ) -> StageGetSchema | None:
        return await get_stage_service().delete(uuid)
