import strawberry

from api.stages.dependencies import get_stage_service
from api.stages.types.request import StageSchema, StageOptionalSchema
from api.stages.types.response import StageGetSchema


@strawberry.type
class StageMutation:
    @strawberry.mutation
    async def create(
        self,
        schema: StageSchema
    ) -> StageGetSchema | None:
        return await get_stage_service().create(schema)

    @strawberry.mutation
    async def update(
        self,
        uuid: str,
        schema: StageOptionalSchema
    ) -> StageGetSchema | None:
        return await get_stage_service().update(uuid, schema)

    @strawberry.mutation
    async def delete(
        self,
        uuid: str
    ) -> StageGetSchema | None:
        return await get_stage_service().delete(uuid)
