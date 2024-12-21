import strawberry

from api.auth.users.dependencies import get_user_service
from api.auth.users.schemas import UserCreateSchema, UserUpdateSchema, UserGetSchema
from api.auth.utils import requires_admin


@strawberry.type
class UserMutation:
    @strawberry.mutation
    @requires_admin
    async def create(
        self,
        info: strawberry.Info,
        schema: UserCreateSchema
    ) -> UserGetSchema | None:
        return await get_user_service().create(schema)

    @strawberry.mutation
    @requires_admin
    async def update(
        self,
        info: strawberry.Info,
        uuid: str,
        schema: UserUpdateSchema
    ) -> UserGetSchema | None:
        return await get_user_service().update(uuid, schema)

    @strawberry.mutation
    @requires_admin
    async def delete(
        self,
        info: strawberry.Info,
        uuid: str
    ) -> UserGetSchema | None:
        return await get_user_service().delete(uuid)
