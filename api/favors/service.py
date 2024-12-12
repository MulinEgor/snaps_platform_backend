from uuid import UUID
from strawberry.exceptions import GraphQLError

from api.favors.repository import FavorRepository
from api.favors.types.response import FavorGetSchema
from api.favors.types.request import FavorCreateSchema, FavorUpdateSchema
from api.logger import get_logger


class FavorService:
    def __init__(self, repository: FavorRepository):
        self.repository = repository
        self.logger = get_logger(__name__)

    async def get(self, uuid: str) -> FavorGetSchema | None:
        favor = await self.repository.get(uuid)
        if not favor:
            self.handle_error(f"Favor with uuid: {uuid} not found")
        return favor

    async def get_all(self) -> list[FavorGetSchema] | None:
        favors = await self.repository.get_all()
        if not favors:
            self.handle_error("No favors found")
        return favors

    async def create(self, data: FavorCreateSchema) -> FavorGetSchema | None:
        favor = await self.repository.create(data)
        if not favor:
            self.handle_error("Failed to create favor")
        return favor

    async def update(self, uuid: str, data: FavorUpdateSchema) -> FavorGetSchema | None:
        if not await self.get(uuid):
            self.handle_error(f"Favor with uuid: {uuid} not found")

        favor = await self.repository.update(uuid, data)
        self.logger.info(favor)
        if not favor:
            self.handle_error(f"Failed to update favor with uuid: {uuid}")
        return favor

    async def delete(self, uuid: str) -> FavorGetSchema | None:
        if not await self.get(uuid):
            self.handle_error(f"Favor with uuid: {uuid} not found")

        favor = await self.repository.delete(uuid)
        if not favor:
            self.handle_error(f"Failed to delete favor with uuid: {uuid}")
        return favor

    def handle_error(self, message: str):
        self.logger.error(message)
        raise GraphQLError(message)
