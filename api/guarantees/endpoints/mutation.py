import strawberry

from api.auth.utils import requires_admin
from api.guarantees.dependencies import get_guarantee_service
from api.guarantees.schemas import GuaranteeGetSchema, GuaranteeCreateSchema, GuaranteeUpdateSchema


@strawberry.type
class GuaranteeMutation:
    @strawberry.mutation
    @requires_admin
    async def create(
        self,
        info: strawberry.Info,
        schema: GuaranteeCreateSchema
    ) -> GuaranteeGetSchema | None:
        return await get_guarantee_service().create(schema)

    @strawberry.mutation
    @requires_admin
    async def update(
        self,
        info: strawberry.Info,
        uuid: str,
        schema: GuaranteeUpdateSchema
    ) -> GuaranteeGetSchema | None:
        return await get_guarantee_service().update(uuid, schema)

    @strawberry.mutation
    @requires_admin
    async def delete(
        self,
        info: strawberry.Info,
        uuid: str
    ) -> GuaranteeGetSchema | None:
        return await get_guarantee_service().delete(uuid)
