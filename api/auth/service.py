from api.auth.jwt.schemas import JWTCreateSchema
from api.auth.jwt.service import JWTService
from api.auth.schemas import AuthGetSchema
from api.auth.users.schemas import UserLoginSchema
from api.auth.users.service import UserService
from api.service import Service


class AuthService(Service):
    def __init__(self, user_service: UserService, jwt_service: JWTService):
        super().__init__(self.__class__.__name__, None)
        self._user_service = user_service
        self._jwt_service = jwt_service

    async def login(self, schema: UserLoginSchema) -> AuthGetSchema | None:
        user = await self._user_service.login(schema)
        print(user)
        tokens = self._jwt_service.create_tokens(
            JWTCreateSchema(
                uuid=user.uuid,
                role_name=user.role.name
            )
        )
        return AuthGetSchema(user=user, tokens=tokens)
