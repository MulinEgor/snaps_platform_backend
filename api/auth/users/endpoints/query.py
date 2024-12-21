import strawberry

from api.auth.users.dependencies import get_user_service
from api.auth.users.schemas import UserUpdateSchema, UserGetSchema
from api.auth.utils import requires_admin


@strawberry.type
class UserQuery:
    @strawberry.field
    @requires_admin
    async def users(
        self,
        info: strawberry.Info,
        filters: UserUpdateSchema
    ) -> list[UserGetSchema]:
        return await get_user_service().get_all(filters)
