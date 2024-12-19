import strawberry
import strawberry.field_extensions

from api.favors.dependencies import get_favor_service
from api.favors.schemas import FavorUpdateSchema, FavorGetSchema


@strawberry.type
class FavorQuery:
    @strawberry.field
    async def favors(
        self,
        filters: FavorUpdateSchema
    ) -> list[FavorGetSchema]:
        return await get_favor_service().get_all(filters)
