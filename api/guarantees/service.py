from api.guarantees.repository import GuaranteeRepository
from api.guarantees.schemas import GuaranteeCreateSchema, GuaranteeUpdateSchema, GuaranteeGetSchema
from api.service import Service


class GuaranteeService(Service):
    def __init__(self, repository: GuaranteeRepository):
        super().__init__(self.__class__.__name__, repository)
        self._repository: GuaranteeRepository

    async def get(self, uuid: str) -> GuaranteeGetSchema | None:
        return await super().get(uuid)

    async def get_all(self, filters: GuaranteeUpdateSchema) -> list[GuaranteeGetSchema] | None:
        return await super().get_all(filters)

    async def create(self, data: GuaranteeCreateSchema) -> GuaranteeGetSchema | None:
        return await super().create(data)

    async def update(self, uuid: str, data: GuaranteeUpdateSchema) -> GuaranteeGetSchema | None:
        return await super().update(uuid, data)

    async def delete(self, uuid: str) -> GuaranteeGetSchema | None:
        return await super().delete(uuid)
