from prisma.models import Favor

from api.favors.schemas import FavorCreateSchema, FavorUpdateSchema
from api.repository import Repository


class FavorRepository(Repository):
    def __init__(self):
        super().__init__('favor')

    async def get(self, uuid: str) -> Favor | None:
        return await super().get(uuid)

    async def get_all(self, filters: FavorUpdateSchema) -> list[Favor]:
        return await super().get_all(filters.to_dict())

    async def create(self, data: FavorCreateSchema) -> Favor:
        return await super().create(data.__dict__)

    async def update(self, uuid: str, data: FavorUpdateSchema) -> Favor:
        return await super().update(uuid, data.to_dict())

    async def delete(self, uuid: str) -> Favor:
        return await super().delete(uuid)
