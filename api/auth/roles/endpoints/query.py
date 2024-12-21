import strawberry
import strawberry.field_extensions

from api.auth.roles.dependencies import get_role_service
from api.auth.roles.schemas import RoleGetSchema
from api.auth.utils import requires_admin


@strawberry.type
class RoleQuery:
    @strawberry.field
    @requires_admin
    async def roles(
        self,
        info: strawberry.Info
    ) -> list[RoleGetSchema]:
        return await get_role_service().get_all()
