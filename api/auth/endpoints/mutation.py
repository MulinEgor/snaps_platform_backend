import strawberry

from api.auth.jwt.dependencies import get_jwt_service
from api.auth.dependencies import get_auth_service
from api.auth.jwt.schemas import JWTGetSchema
from api.auth.schemas import AuthGetSchema
from api.auth.users.schemas import UserLoginSchema


@strawberry.type
class AuthMutation:
    @strawberry.mutation
    async def login(
        self,
        schema: UserLoginSchema
    ) -> AuthGetSchema | None:
        return await get_auth_service().login(schema)

    @strawberry.mutation
    async def refresh(
        self,
        refresh_token: str
    ) -> JWTGetSchema | None:
        return get_jwt_service().refresh_tokens(refresh_token)
