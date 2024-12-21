import strawberry

from api.auth.utils import requires_admin
from api.favors.dependencies import get_favor_service
from api.favors.schemas import FavorCreateSchema, FavorUpdateSchema, FavorGetSchema


@strawberry.type
class FavorMutation:
    @strawberry.mutation
    @requires_admin
    async def create(
        self,
        info: strawberry.Info,
        schema: FavorCreateSchema
    ) -> FavorGetSchema | None:
        return await get_favor_service().create(schema)

    @strawberry.mutation
    @requires_admin
    async def update(
        self,
        info: strawberry.Info,
        uuid: str,
        schema: FavorUpdateSchema
    ) -> FavorGetSchema | None:
        return await get_favor_service().update(uuid, schema)

    @strawberry.mutation
    @requires_admin
    async def delete(
        self,
        info: strawberry.Info,
        uuid: str
    ) -> FavorGetSchema | None:
        return await get_favor_service().delete(uuid)
