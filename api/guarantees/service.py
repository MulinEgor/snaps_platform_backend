from api.guarantees.repository import GuaranteeRepository
from api.guarantees.types.response import GuaranteeGetSchema
from api.guarantees.types.request import GuaranteeSchema, GuaranteeOptionalSchema
from api.service import Service


class GuaranteeService(Service):
    def __init__(self, repository: GuaranteeRepository):
        super().__init__(self.__class__.__name__, repository)
        self.repository: GuaranteeRepository

    async def get(self, uuid: str) -> GuaranteeGetSchema | None:
        self.logger.info(f"Fetching guarantee with uuid: {uuid}")
        guarantee = await self.repository.get(uuid)
        if not guarantee:
            self.handle_error(f"Guarantee with uuid: {uuid} not found")
        self.logger.info(f"Guarantee with uuid: {uuid} retrieved successfully")
        return guarantee

    async def get_all(self, filters: GuaranteeOptionalSchema) -> list[GuaranteeGetSchema] | None:
        self.logger.info(f"Fetching all guarantees with filters: \n{
                         filters.to_dict()}")
        guarantees = await self.repository.get_all(filters)
        if not guarantees:
            self.handle_error("No guarantees found")
        self.logger.info(f"Retrieved {len(guarantees)} guarantees")
        return guarantees

    async def create(self, data: GuaranteeSchema) -> GuaranteeGetSchema | None:
        self.logger.info(f"Creating guarantee with data: \n{data.__dict__()}")
        guarantee = await self.repository.create(data)
        if not guarantee:
            self.handle_error("Failed to create guarantee")
        self.logger.info(f"Guarantee created successfully with uuid: {
                         guarantee.uuid}")
        return guarantee

    async def update(self, uuid: str, data: GuaranteeOptionalSchema) -> GuaranteeGetSchema | None:
        self.logger.info(f"Updating guarantee with uuid: {
                         uuid} and data: \n{data.to_dict()}")
        await self.get(uuid)

        guarantee = await self.repository.update(uuid, data)
        if not guarantee:
            self.handle_error(f"Failed to update guarantee with uuid: {uuid}")
        self.logger.info(f"Guarantee with uuid: {uuid} updated successfully")
        return guarantee

    async def delete(self, uuid: str) -> GuaranteeGetSchema | None:
        self.logger.info(f"Deleting guarantee with uuid: {uuid}")
        await self.get(uuid)

        guarantee = await self.repository.delete(uuid)
        if not guarantee:
            self.handle_error(f"Failed to delete guarantee with uuid: {uuid}")
        self.logger.info(f"Guarantee with uuid: {uuid} deleted successfully")
        return guarantee
