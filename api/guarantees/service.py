from api.guarantees.repository import GuaranteeRepository
from api.guarantees.types.response import GuaranteeGetSchema
from api.guarantees.types.request import GuaranteeSchema, GuaranteeOptionalSchema
from api.service import Service


class GuaranteeService(Service):
    def __init__(self, repository: GuaranteeRepository):
        super().__init__(self.__class__.__name__, repository)
        self.repository: GuaranteeRepository

    async def get(self, uuid: str) -> GuaranteeGetSchema | None:
        self.logger.info(f"Fetching data with uuid: {uuid}")
        guarantee = await self.repository.get(uuid)
        if not guarantee:
            self.handle_error(f"Data with uuid: {uuid} not found")
        self.logger.info(f"Data with uuid: {uuid} retrieved successfully")
        return guarantee

    async def get_all(self, filters: GuaranteeOptionalSchema) -> list[GuaranteeGetSchema] | None:
        self.logger.info(f"Fetching all data with filters: \n{
                         filters.to_dict()}")
        guarantees = await self.repository.get_all(filters)
        if not guarantees:
            self.handle_error("No data found")
        self.logger.info(f"Retrieved data with size {len(guarantees)}")
        return guarantees

    async def create(self, data: GuaranteeSchema) -> GuaranteeGetSchema | None:
        self.logger.info(f"Creating data: \n{data.__dict__()}")
        guarantee = await self.repository.create(data)
        if not guarantee:
            self.handle_error("Failed to create")
        self.logger.info(f"Data created successfully with uuid: {
                         guarantee.uuid}")
        return guarantee

    async def update(self, uuid: str, data: GuaranteeOptionalSchema) -> GuaranteeGetSchema | None:
        self.logger.info(f"Updating data with uuid: {
                         uuid} and data: \n{data.to_dict()}")
        await self.get(uuid)

        guarantee = await self.repository.update(uuid, data)
        if not guarantee:
            self.handle_error(f"Failed to update data with uuid: {uuid}")
        self.logger.info(f"Data with uuid: {uuid} updated successfully")
        return guarantee

    async def delete(self, uuid: str) -> GuaranteeGetSchema | None:
        self.logger.info(f"Deleting data with uuid: {uuid}")
        await self.get(uuid)

        guarantee = await self.repository.delete(uuid)
        if not guarantee:
            self.handle_error(f"Failed to delete data with uuid: {uuid}")
        self.logger.info(f"Data with uuid: {uuid} deleted successfully")
        return guarantee
