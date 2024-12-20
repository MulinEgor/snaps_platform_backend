import strawberry

from api.auth.roles.dependencies import get_role_service
from api.auth.roles.schemas import RoleCreateSchema, RoleGetSchema


@strawberry.type
class RoleMutation:
    @strawberry.mutation
    async def create(
        self,
        schema: RoleCreateSchema
    ) -> RoleGetSchema | None:
        return await get_role_service().create(schema)

    @strawberry.mutation
    async def delete(
        self,
        uuid: str
    ) -> RoleGetSchema | None:
        return await get_role_service().delete(uuid)
