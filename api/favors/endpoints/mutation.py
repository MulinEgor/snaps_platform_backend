import strawberry

from api.favors.repository import FavorRepository
from api.favors.types.request import FavorCreateSchema, FavorOptionalSchema
from api.favors.service import FavorService
from api.favors.types.response import FavorGetSchema


@strawberry.type
class FavorMutation:
    @strawberry.mutation
    async def create_favor(
        self,
        schema: FavorCreateSchema
    ) -> FavorGetSchema | None:
        service = FavorService(FavorRepository())
        return await service.create(schema)

    @strawberry.mutation
    async def update_favor(
        self,
        uuid: str,
        schema: FavorOptionalSchema
    ) -> FavorGetSchema | None:
        service = FavorService(FavorRepository())
        return await service.update(uuid, schema)

    @strawberry.mutation
    async def delete_favor(
        self,
        uuid: str
    ) -> FavorGetSchema | None:
        service = FavorService(FavorRepository())
        return await service.delete(uuid)
