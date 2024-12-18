import strawberry

from api.stages.dependencies import get_stage_service
from api.stages.types.request import StageOptionalSchema
from api.stages.types.response import StageGetSchema


@strawberry.type
class StageQuery:
    @strawberry.field
    async def stages(
        self,
        filters: StageOptionalSchema
    ) -> list[StageGetSchema]:
        return await get_stage_service().get_all(filters)
