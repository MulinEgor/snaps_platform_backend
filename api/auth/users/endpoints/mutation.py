import strawberry

from api.auth.users.dependencies import get_user_service
from api.auth.users.schemas import UserCreateSchema, UserUpdateSchema, UserGetSchema


@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def create(
        self,
        schema: UserCreateSchema
    ) -> UserGetSchema | None:
        return await get_user_service().create(schema)

    @strawberry.mutation
    async def update(
        self,
        uuid: str,
        schema: UserUpdateSchema
    ) -> UserGetSchema | None:
        return await get_user_service().update(uuid, schema)

    @strawberry.mutation
    async def delete(
        self,
        uuid: str
    ) -> UserGetSchema | None:
        return await get_user_service().delete(uuid)
