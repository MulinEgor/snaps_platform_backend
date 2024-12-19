from api.requests.repository import RequestRepository
from api.requests.schemas import RequestCreateSchema, RequestUpdateSchema, RequestGetSchema
from api.service import Service


class RequestService(Service):
    def __init__(self, repository: RequestRepository):
        super().__init__(self.__class__.__name__, repository)
        self._repository: RequestRepository

    async def get(self, uuid: str) -> RequestGetSchema | None:
        return super().get(uuid)

    async def get_all(self, filters: RequestUpdateSchema) -> list[RequestGetSchema] | None:
        return super().get_all(filters)

    async def create(self, data: RequestCreateSchema) -> RequestGetSchema | None:
        return super().create(data)

    async def update(self, uuid: str, data: RequestUpdateSchema) -> RequestGetSchema | None:
        return super().update(uuid, data)

    async def delete(self, uuid: str) -> RequestGetSchema | None:
        return super().delete(uuid)
