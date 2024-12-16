import strawberry

from api.favors.dependencies import get_favor_service
from api.favors.types.request import FavorCreateSchema, FavorOptionalSchema
from api.favors.types.response import FavorGetSchema


@strawberry.type
class FavorMutation:
    @strawberry.mutation
    async def create(
        self,
        schema: FavorCreateSchema
    ) -> FavorGetSchema | None:
        return await get_favor_service().create(schema)

    @strawberry.mutation
    async def update(
        self,
        uuid: str,
        schema: FavorOptionalSchema
    ) -> FavorGetSchema | None:
        return await get_favor_service().update(uuid, schema)

    @strawberry.mutation
    async def delete(
        self,
        uuid: str
    ) -> FavorGetSchema | None:
        return await get_favor_service().delete(uuid)
