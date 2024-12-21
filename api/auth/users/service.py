import hashlib

from api.auth.roles.service import RoleService
from api.auth.users.repository import UserRepository
from api.auth.users.schemas import UserCreateORMSchema, UserGetSchema, UserCreateSchema, UserLoginSchema, UserUpdateORMSchema, UserUpdateSchema
from api.service import Service


class UserService(Service):
    def __init__(self, repository: UserRepository, role_service: RoleService):
        super().__init__(self.__class__.__name__, repository)
        self._repository: UserRepository
        self._role_service: RoleService = role_service

    async def get(self, uuid: str) -> UserGetSchema | None:
        return await super().get(uuid)

    async def login(self, schema: UserLoginSchema) -> UserGetSchema | None:
        user = await self._repository.get_by_email(schema.email)
        if not user or user.hashed_password != self.hash_password(schema.password):
            self._handle_error('Invalid email or password')
        return user

    async def get_all(self, filters: UserUpdateSchema) -> list[UserGetSchema]:
        prepared_data = UserUpdateORMSchema(
            email=filters.email,
            hashed_password=UserService.hash_password(
                filters.password
            ) if filters.password else None,
            role_uuid=filters.role_uuid
        )
        return await super().get_all(prepared_data)

    async def create(self, data: UserCreateSchema) -> UserGetSchema | None:
        if await self._repository.exists(data.email):  # check if user exists
            self._handle_error('User with this email already exists')
        await self._role_service.get(data.role_uuid)  # check if role exists
        prepared_data = UserCreateORMSchema(
            email=data.email,
            hashed_password=UserService.hash_password(
                data.password
            ) if data.password else None,
            role_uuid=data.role_uuid
        )

        return await super().create(prepared_data)

    async def update(self, uuid: str, data: UserUpdateSchema) -> UserGetSchema | None:
        user = await self.get(uuid)
        # check for new email uniqness
        if not user or (user.email != data.email and await self._repository.exists(data.email)):
            self._handle_error('User with this email already exists')
        await self._role_service.get(data.role_uuid)  # check if role exists
        prepared_data = UserUpdateORMSchema(
            email=data.email,
            hashed_password=UserService.hash_password(
                data.password
            ) if data.password else None,
            role_uuid=data.role_uuid
        )

        return await super().update(uuid, prepared_data)

    async def delete(self, uuid: str) -> UserGetSchema | None:
        return await super().delete(uuid)

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.md5(password.encode('utf-8')).hexdigest()
