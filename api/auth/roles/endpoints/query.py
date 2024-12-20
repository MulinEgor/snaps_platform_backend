import strawberry
import strawberry.field_extensions

from api.auth.roles.dependencies import get_role_service
from api.auth.roles.schemas import RoleGetSchema


@strawberry.type
class RoleQuery:
    @strawberry.field
    async def roles(
        self,
    ) -> list[RoleGetSchema]:
        return await get_role_service().get_all()
