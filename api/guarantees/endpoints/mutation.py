import strawberry

from api.guarantees.dependencies import get_guarantee_service
from api.guarantees.schemas import GuaranteeGetSchema, GuaranteeCreateSchema, GuaranteeUpdateSchema


@strawberry.type
class GuaranteeMutation:
    @strawberry.mutation
    async def create(
        self,
        schema: GuaranteeCreateSchema
    ) -> GuaranteeGetSchema | None:
        return await get_guarantee_service().create(schema)

    @strawberry.mutation
    async def update(
        self,
        uuid: str,
        schema: GuaranteeUpdateSchema
    ) -> GuaranteeGetSchema | None:
        return await get_guarantee_service().update(uuid, schema)

    @strawberry.mutation
    async def delete(
        self,
        uuid: str
    ) -> GuaranteeGetSchema | None:
        return await get_guarantee_service().delete(uuid)
