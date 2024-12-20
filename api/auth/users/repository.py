from prisma.models import User

from api.auth.users.schemas import UserCreateORMSchema, UserUpdateORMSchema
from api.database import db_session
from api.repository import Repository


class UserRepository(Repository):
    include = {
        'role': True
    }

    def __init__(self):
        super().__init__('user')

    async def get(self, uuid: str) -> User | None:
        return await super().get(uuid)

    async def get_by_email(self, email: str) -> User | None:
        async with db_session() as session:
            return await session.user.find_first(where={'email': email}, include=self.include)

    async def get_all(self, filters: UserUpdateORMSchema) -> list[User]:
        return await super().get_all(filters.to_dict())

    async def create(self, data: UserCreateORMSchema) -> User:
        return await super().create(data.__dict__)

    async def update(self, uuid: str, data: UserUpdateORMSchema) -> User:
        return await super().update(uuid, data.to_dict())

    async def delete(self, uuid: str) -> User:
        return await super().delete(uuid)

    async def exists(self, email: str) -> bool:
        async with db_session() as session:
            return await session.user.find_first(where={'email': email}) is not None
