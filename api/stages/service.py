from api.stages.repository import StageRepository
from api.stages.types.response import StageGetSchema
from api.stages.types.request import StageSchema, StageOptionalSchema
from api.service import Service


class StageService(Service):
    def __init__(self, repository: StageRepository):
        super().__init__(self.__class__.__name__, repository)
        self._repository: StageRepository

    async def get(self, uuid: str) -> StageGetSchema | None:
        self._logger.info(f"Fetching data with uuid: {uuid}")
        stage = await self._repository.get(uuid)
        if not stage:
            self._handle_error(f"Data with uuid: {uuid} not found")
        self._logger.info(f"Data with uuid: {uuid} retrieved successfully")
        return stage

    async def get_all(self, filters: StageOptionalSchema) -> list[StageGetSchema] | None:
        self._logger.info(f"Fetching all data with filters: \n{
            filters.to_dict()}")
        stages = await self._repository.get_all(filters)
        if not stages:
            self._handle_error("No data found")
        self._logger.info(f"Retrieved data with size {len(stages)}")
        return stages

    async def create(self, data: StageSchema) -> StageGetSchema | None:
        self._logger.info(f"Creating data: \n{data.__dict__()}")
        stage = await self._repository.create(data)
        if not stage:
            self._handle_error("Failed to create")
        self._logger.info(f"Data created successfully with uuid: {
            stage.uuid}")
        return stage

    async def update(self, uuid: str, data: StageOptionalSchema) -> StageGetSchema | None:
        self._logger.info(f"Updating data with uuid: {
            uuid} and data: \n{data.to_dict()}")
        await self.get(uuid)

        stage = await self._repository.update(uuid, data)
        if not stage:
            self._handle_error(f"Failed to update data with uuid: {uuid}")
        self._logger.info(f"Data with uuid: {uuid} updated successfully")
        return stage

    async def delete(self, uuid: str) -> StageGetSchema | None:
        self._logger.info(f"Deleting data with uuid: {uuid}")
        await self.get(uuid)

        stage = await self._repository.delete(uuid)
        if not stage:
            self._handle_error(f"Failed to delete data with uuid: {uuid}")
        self._logger.info(f"Data with uuid: {uuid} deleted successfully")
        return stage
