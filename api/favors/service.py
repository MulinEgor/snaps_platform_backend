from api.favors.repository import FavorRepository
from api.favors.types.response import FavorGetSchema
from api.favors.types.request import FavorSchema, FavorOptionalSchema
from api.service import Service


class FavorService(Service):
    def __init__(self, repository: FavorRepository):
        super().__init__(self.__class__.__name__, repository)
        self._repository: FavorRepository

    async def get(self, uuid: str) -> FavorGetSchema | None:
        self._logger.info(f"Fetching data with uuid: {uuid}")
        favor = await self._repository.get(uuid)
        if not favor:
            self._handle_error(f"Data with uuid: {uuid} not found")
        self._logger.info(f"Data with uuid: {uuid} retrieved successfully")
        return favor

    async def get_all(self, filters: FavorOptionalSchema) -> list[FavorGetSchema] | None:
        self._logger.info(f"Fetching all data with filters: \n{
            filters.to_dict()}")
        favors = await self._repository.get_all(filters)
        if not favors:
            self._handle_error("No data found")
        self._logger.info(f"Retrieved {len(favors)} data")
        return favors

    async def create(self, data: FavorSchema) -> FavorGetSchema | None:
        self._logger.info(f"Creating data: {data}")
        favor = await self._repository.create(data)
        if not favor:
            self._handle_error("Failed to create")
        self._logger.info(f"Data created successfully with uuid: {favor.uuid}")
        return favor

    async def update(self, uuid: str, data: FavorOptionalSchema) -> FavorGetSchema | None:
        self._logger.info(f"Updating data with uuid: {uuid} and data: {data}")
        await self.get(uuid)

        favor = await self._repository.update(uuid, data)
        if not favor:
            self._handle_error(f"Failed to update data with uuid: {uuid}")
        self._logger.info(f"Data with uuid: {uuid} updated successfully")
        return favor

    async def delete(self, uuid: str) -> FavorGetSchema | None:
        self._logger.info(f"Deleting data with uuid: {uuid}")
        await self.get(uuid)

        favor = await self._repository.delete(uuid)
        if not favor:
            self._handle_error(f"Failed to delete data with uuid: {uuid}")
        self._logger.info(f"Data with uuid: {uuid} deleted successfully")
        return favor
