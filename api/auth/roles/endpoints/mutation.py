import strawberry

from api.auth.roles.dependencies import get_role_service
from api.auth.roles.schemas import RoleCreateSchema, RoleGetSchema
from api.auth.utils import requires_admin


@strawberry.type
class RoleMutation:
    @strawberry.mutation
    @requires_admin
    async def create(
        self,
        info: strawberry.Info,
        schema: RoleCreateSchema
    ) -> RoleGetSchema | None:
        return await get_role_service().create(schema)

    @strawberry.mutation
    @requires_admin
    async def delete(
        self,
        info: strawberry.Info,
        uuid: str
    ) -> RoleGetSchema | None:
        return await get_role_service().delete(uuid)
