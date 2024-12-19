import strawberry

from api.requests.dependencies import get_request_service
from api.requests.schemas import RequestUpdateSchema, RequestGetSchema


@strawberry.type
class RequestQuery:
    @strawberry.field
    async def requests(
        self,
        filters: RequestUpdateSchema
    ) -> list[RequestGetSchema]:
        return await get_request_service().get_all(filters)
