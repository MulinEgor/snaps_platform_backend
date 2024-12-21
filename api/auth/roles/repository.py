from prisma.models import Role

from api.auth.roles.schemas import RoleCreateSchema
from api.repository import Repository


class RoleRepository(Repository):
    def __init__(self):
        super().__init__('role')

    async def get(self, uuid: str) -> Role | None:
        return await super().get(uuid)

    async def get_all(self) -> list[Role]:
        return await super().get_all({})

    async def create(self, data: RoleCreateSchema) -> Role:
        return await super().create(data.__dict__)

    async def delete(self, uuid: str) -> Role:
        return await super().delete(uuid)
