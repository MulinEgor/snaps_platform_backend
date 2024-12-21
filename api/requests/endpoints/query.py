import strawberry

from api.auth.utils import requires_admin
from api.requests.dependencies import get_request_service
from api.requests.schemas import RequestUpdateSchema, RequestGetSchema


@strawberry.type
class RequestQuery:
    @strawberry.field
    @requires_admin
    async def requests(
        self,
        info: strawberry.Info,
        filters: RequestUpdateSchema
    ) -> list[RequestGetSchema]:
        return await get_request_service().get_all(filters)
