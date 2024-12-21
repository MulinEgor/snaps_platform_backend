from strawberry.exceptions import GraphQLError

from api.logger import get_logger
from api.repository import Repository


class Service:
    def __init__(self, name: str, repository: Repository):
        self._logger = get_logger(name)
        self._repository = repository

    async def get(self, uuid: str) -> any:
        self._logger.info(f"Fetching data with uuid: {uuid}")
        data = await self._repository.get(uuid)
        if not data:
            self._handle_error(f"Data with uuid: {uuid} not found")
        self._logger.info(f"Data with uuid: {uuid} retrieved successfully")
        return data

    async def get_all(self, filters: any) -> list[any]:
        self._logger.info(f"Fetching all data with filters: \n{
            filters.to_dict()}")
        data = await self._repository.get_all(filters)
        self._logger.info(f"Retrieved {len(data)} data")
        return data

    async def create(self, data: any) -> any:
        self._logger.info(f"Creating data: {data}")
        data = await self._repository.create(data)
        if not data:
            self._handle_error("Failed to create")
        self._logger.info(f"Data created successfully with uuid: {data.uuid}")
        return data

    async def update(self, uuid: str, data: any) -> any:
        self._logger.info(f"Updating data with uuid: {uuid} and data: {data}")
        await self.get(uuid)

        data = await self._repository.update(uuid, data)
        if not data:
            self._handle_error(f"Failed to update data with uuid: {uuid}")
        self._logger.info(f"Data with uuid: {uuid} updated successfully")
        return data

    async def delete(self, uuid: str) -> any:
        self._logger.info(f"Deleting data with uuid: {uuid}")
        await self.get(uuid)

        data = await self._repository.delete(uuid)
        if not data:
            self._handle_error(f"Failed to delete data with uuid: {uuid}")
        self._logger.info(f"Data with uuid: {uuid} deleted successfully")
        return data

    def _handle_error(self, message: str):
        self._logger.error(message)
        raise GraphQLError(message)
