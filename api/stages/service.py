from api.stages.repository import StageRepository
from api.stages.schemas import StageCreateSchema, StageUpdateSchema, StageGetSchema
from api.service import Service


class StageService(Service):
    def __init__(self, repository: StageRepository):
        super().__init__(self.__class__.__name__, repository)
        self._repository: StageRepository

    async def get(self, uuid: str) -> StageGetSchema | None:
        return await super().get(uuid)

    async def get_all(self, filters: StageUpdateSchema) -> list[StageGetSchema]:
        return await super().get_all(filters)

    async def create(self, data: StageCreateSchema) -> StageGetSchema | None:
        return await super().create(data)

    async def update(self, uuid: str, data: StageUpdateSchema) -> StageGetSchema | None:
        return await super().update(uuid, data)

    async def delete(self, uuid: str) -> StageGetSchema | None:
        return await super().delete(uuid)
