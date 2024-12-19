import strawberry

from api.guarantees.dependencies import get_guarantee_service
from api.guarantees.schemas import GuaranteeUpdateSchema, GuaranteeGetSchema


@strawberry.type
class GuaranteeQuery:
    @strawberry.field
    async def guarantees(
        self,
        filters: GuaranteeUpdateSchema
    ) -> list[GuaranteeGetSchema]:
        return await get_guarantee_service().get_all(filters)
