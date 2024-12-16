from prisma.models import Guarantee

from api.guarantees.types.request import GuaranteeSchema, GuaranteeOptionalSchema
from api.repository import Repository


class GuaranteeRepository(Repository):
    def __init__(self):
        super().__init__('guarantee')

    async def get(self, uuid: str) -> Guarantee | None:
        return await super().get(uuid)

    async def get_all(self, filters: GuaranteeOptionalSchema) -> list[Guarantee] | None:
        return await super().get_all(filters.to_dict())

    async def create(self, data: GuaranteeSchema) -> Guarantee:
        return await super().create(data.__dict__)

    async def update(self, uuid: str, data: GuaranteeOptionalSchema) -> Guarantee:
        return await super().update(uuid, data.to_dict())

    async def delete(self, uuid: str) -> Guarantee:
        return await super().delete(uuid)
