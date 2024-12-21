from api.favors.repository import FavorRepository
from api.favors.schemas import FavorGetSchema, FavorCreateSchema, FavorUpdateSchema
from api.service import Service


class FavorService(Service):
    def __init__(self, repository: FavorRepository):
        super().__init__(self.__class__.__name__, repository)
        self._repository: FavorRepository

    async def get(self, uuid: str) -> FavorGetSchema | None:
        return await super().get(uuid)

    async def get_all(self, filters: FavorUpdateSchema) -> list[FavorGetSchema]:
        return await super().get_all(filters)

    async def create(self, data: FavorCreateSchema) -> FavorGetSchema | None:
        return await super().create(data)

    async def update(self, uuid: str, data: FavorUpdateSchema) -> FavorGetSchema | None:
        return await super().update(uuid, data)

    async def delete(self, uuid: str) -> FavorGetSchema | None:
        return await super().delete(uuid)
