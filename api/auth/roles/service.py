from api.auth.roles.repository import RoleRepository
from api.auth.roles.schemas import RoleGetSchema, RoleCreateSchema
from api.service import Service


class RoleService(Service):
    def __init__(self, repository: RoleRepository):
        super().__init__(self.__class__.__name__, repository)
        self._repository: RoleRepository

    async def get(self, uuid: str) -> RoleGetSchema | None:
        return await super().get(uuid)

    async def get_all(self) -> list[RoleGetSchema]:
        self._logger.info(f"Fetching all data")
        data = await self._repository.get_all()
        if not data:
            data = []
        self._logger.info(f"Retrieved {len(data)} data")
        return data

    async def create(self, data: RoleCreateSchema) -> RoleGetSchema | None:
        return await super().create(data)

    async def delete(self, uuid: str) -> RoleGetSchema | None:
        return await super().delete(uuid)
