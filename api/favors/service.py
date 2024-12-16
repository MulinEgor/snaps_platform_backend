from api.favors.repository import FavorRepository
from api.favors.types.response import FavorGetSchema
from api.favors.types.request import FavorCreateSchema, FavorOptionalSchema
from api.service import Service


class FavorService(Service):
    def __init__(self, repository: FavorRepository):
        super().__init__(self.__class__.__name__, repository)
        self.repository: FavorRepository

    async def get(self, uuid: str) -> FavorGetSchema | None:
        self.logger.info(f"Fetching favor with uuid: {uuid}")
        favor = await self.repository.get(uuid)
        if not favor:
            self.handle_error(f"Favor with uuid: {uuid} not found")
        self.logger.info(f"Favor with uuid: {uuid} retrieved successfully")
        return favor

    async def get_all(self, filters: FavorOptionalSchema) -> list[FavorGetSchema] | None:
        self.logger.info(f"Fetching all favors with filters: \n{
                         filters.to_dict()}")
        favors = await self.repository.get_all(filters)
        if not favors:
            self.handle_error("No favors found")
        self.logger.info(f"Retrieved {len(favors)} favors")
        return favors

    async def create(self, data: FavorCreateSchema) -> FavorGetSchema | None:
        self.logger.info(f"Creating favor with data: {data}")
        favor = await self.repository.create(data)
        if not favor:
            self.handle_error("Failed to create favor")
        self.logger.info(f"Favor created successfully with uuid: {favor.uuid}")
        return favor

    async def update(self, uuid: str, data: FavorOptionalSchema) -> FavorGetSchema | None:
        self.logger.info(f"Updating favor with uuid: {uuid} and data: {data}")
        await self.get(uuid)

        favor = await self.repository.update(uuid, data)
        if not favor:
            self.handle_error(f"Failed to update favor with uuid: {uuid}")
        self.logger.info(f"Favor with uuid: {uuid} updated successfully")
        return favor

    async def delete(self, uuid: str) -> FavorGetSchema | None:
        self.logger.info(f"Deleting favor with uuid: {uuid}")
        await self.get(uuid)

        favor = await self.repository.delete(uuid)
        if not favor:
            self.handle_error(f"Failed to delete favor with uuid: {uuid}")
        self.logger.info(f"Favor with uuid: {uuid} deleted successfully")
        return favor
