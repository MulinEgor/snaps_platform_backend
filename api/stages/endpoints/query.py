import strawberry

from api.stages.dependencies import get_stage_service
from api.stages.schemas import StageUpdateSchema, StageGetSchema


@strawberry.type
class StageQuery:
    @strawberry.field
    async def stages(
        self,
        filters: StageUpdateSchema
    ) -> list[StageGetSchema]:
        return await get_stage_service().get_all(filters)
