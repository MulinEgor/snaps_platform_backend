from prisma.models import Request

from api.requests.schemas import RequestCreateSchema, RequestUpdateSchema
from api.repository import Repository


class RequestRepository(Repository):
    def __init__(self):
        super().__init__('request')

    async def get(self, uuid: str) -> Request | None:
        return await super().get(uuid)

    async def get_all(self, filters: RequestUpdateSchema) -> list[Request] | None:
        return await super().get_all(filters.to_dict())

    async def create(self, data: RequestCreateSchema) -> Request:
        return await super().create(data.__dict__)

    async def update(self, uuid: str, data: RequestUpdateSchema) -> Request:
        return await super().update(uuid, data.to_dict())

    async def delete(self, uuid: str) -> Request:
        return await super().delete(uuid)
