from api.questions.repository import QuestionRepository
from api.questions.types.response import QuestionGetSchema
from api.questions.types.request import QuestionSchema, QuestionOptionalSchema
from api.service import Service


class QuestionService(Service):
    def __init__(self, repository: QuestionRepository):
        super().__init__(self.__class__.__name__, repository)
        self.repository: QuestionRepository

    async def get(self, uuid: str) -> QuestionGetSchema | None:
        self.logger.info(f"Fetching data with uuid: {uuid}")
        question = await self.repository.get(uuid)
        if not question:
            self.handle_error(f"Data with uuid: {uuid} not found")
        self.logger.info(f"Data with uuid: {uuid} retrieved successfully")
        return question

    async def get_all(self, filters: QuestionOptionalSchema) -> list[QuestionGetSchema] | None:
        self.logger.info(f"Fetching all data with filters: \n{
                         filters.to_dict()}")
        questions = await self.repository.get_all(filters)
        if not questions:
            self.handle_error("No data found")
        self.logger.info(f"Retrieved data with size {len(questions)}")
        return questions

    async def create(self, data: QuestionSchema) -> QuestionGetSchema | None:
        self.logger.info(f"Creating data: \n{data.__dict__()}")
        question = await self.repository.create(data)
        if not question:
            self.handle_error("Failed to create")
        self.logger.info(f"Data created successfully with uuid: {
                         question.uuid}")
        return question

    async def update(self, uuid: str, data: QuestionOptionalSchema) -> QuestionGetSchema | None:
        self.logger.info(f"Updating data with uuid: {
                         uuid} and data: \n{data.to_dict()}")
        await self.get(uuid)

        question = await self.repository.update(uuid, data)
        if not question:
            self.handle_error(f"Failed to update data with uuid: {uuid}")
        self.logger.info(f"Data with uuid: {uuid} updated successfully")
        return question

    async def delete(self, uuid: str) -> QuestionGetSchema | None:
        self.logger.info(f"Deleting data with uuid: {uuid}")
        await self.get(uuid)

        question = await self.repository.delete(uuid)
        if not question:
            self.handle_error(f"Failed to delete data with uuid: {uuid}")
        self.logger.info(f"Data with uuid: {uuid} deleted successfully")
        return question
