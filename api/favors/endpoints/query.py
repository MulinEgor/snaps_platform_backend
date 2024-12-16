import strawberry
import strawberry.field_extensions

from api.favors.dependencies import get_favor_service
from api.favors.types.request import FavorOptionalSchema
from api.favors.types.response import FavorGetSchema


@strawberry.type
class FavorQuery:
    @strawberry.field
    async def favors(
        self,
        filters: FavorOptionalSchema
    ) -> list[FavorGetSchema]:
        return await get_favor_service().get_all(filters)
