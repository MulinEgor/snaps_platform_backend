import strawberry

from api.auth.utils import requires_admin
from api.requests.dependencies import get_request_service
from api.requests.schemas import RequestCreateSchema, RequestUpdateSchema, RequestGetSchema


@strawberry.type
class RequestMutation:
    @strawberry.mutation
    async def create(
        self,
        schema: RequestCreateSchema
    ) -> RequestGetSchema | None:
        return await get_request_service().create(schema)

    @strawberry.mutation
    @requires_admin
    async def update(
        self,
        info: strawberry.Info,
        uuid: str,
        schema: RequestUpdateSchema
    ) -> RequestGetSchema | None:
        return await get_request_service().update(uuid, schema)

    @strawberry.mutation
    @requires_admin
    async def delete(
        self,
        info: strawberry.Info,
        uuid: str
    ) -> RequestGetSchema | None:
        return await get_request_service().delete(uuid)
