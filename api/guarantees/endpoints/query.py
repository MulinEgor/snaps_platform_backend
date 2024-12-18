import strawberry

from api.guarantees.dependencies import get_guarantee_service
from api.guarantees.types.request import GuaranteeOptionalSchema
from api.guarantees.types.response import GuaranteeGetSchema


@strawberry.type
class GuaranteeQuery:
    @strawberry.field
    async def guarantees(
        self,
        filters: GuaranteeOptionalSchema
    ) -> list[GuaranteeGetSchema]:
        return await get_guarantee_service().get_all(filters)
