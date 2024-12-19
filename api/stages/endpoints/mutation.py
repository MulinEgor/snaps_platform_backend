import strawberry

from api.stages.dependencies import get_stage_service
from api.stages.schemas import StageCreateSchema, StageUpdateSchema, StageGetSchema


@strawberry.type
class StageMutation:
    @strawberry.mutation
    async def create(
        self,
        schema: StageCreateSchema
    ) -> StageGetSchema | None:
        return await get_stage_service().create(schema)

    @strawberry.mutation
    async def update(
        self,
        uuid: str,
        schema: StageUpdateSchema
    ) -> StageGetSchema | None:
        return await get_stage_service().update(uuid, schema)

    @strawberry.mutation
    async def delete(
        self,
        uuid: str
    ) -> StageGetSchema | None:
        return await get_stage_service().delete(uuid)
