import strawberry
import strawberry.field_extensions

from api.favors.repository import FavorRepository
from api.favors.service import FavorService
from api.favors.types.response import FavorGetSchema


@strawberry.type
class FavorQuery:
    @strawberry.field
    async def favor(
        self,
        uuid: str
    ) -> FavorGetSchema | None:
        service = FavorService(FavorRepository())
        return await service.get(uuid)

    @strawberry.field
    async def favors(
        self
    ) -> list[FavorGetSchema]:
        service = FavorService(FavorRepository())
        return await service.get_all()
