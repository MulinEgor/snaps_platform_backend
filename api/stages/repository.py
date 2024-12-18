from prisma.models import Stage

from api.stages.types.request import StageSchema, StageOptionalSchema
from api.repository import Repository


class StageRepository(Repository):
    def __init__(self):
        super().__init__('stage')

    async def get(self, uuid: str) -> Stage | None:
        return await super().get(uuid)

    async def get_all(self, filters: StageOptionalSchema) -> list[Stage] | None:
        return await super().get_all(filters.to_dict())

    async def create(self, data: StageSchema) -> Stage:
        return await super().create(data.__dict__)

    async def update(self, uuid: str, data: StageOptionalSchema) -> Stage:
        return await super().update(uuid, data.to_dict())

    async def delete(self, uuid: str) -> Stage:
        return await super().delete(uuid)
