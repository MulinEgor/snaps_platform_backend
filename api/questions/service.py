from api.questions.repository import QuestionRepository
from api.questions.schemas import QuestionGetSchema, QuestionCreateSchema, QuestionUpdateSchema
from api.service import Service


class QuestionService(Service):
    def __init__(self, repository: QuestionRepository):
        super().__init__(self.__class__.__name__, repository)
        self._repository: QuestionRepository

    async def get(self, uuid: str) -> QuestionGetSchema | None:
        return await self._repository.get(uuid)

    async def get_all(self, filters: QuestionUpdateSchema) -> list[QuestionGetSchema]:
        return await self._repository.get_all(filters)

    async def create(self, data: QuestionCreateSchema) -> QuestionGetSchema | None:
        return await self._repository.create(data)

    async def update(self, uuid: str, data: QuestionUpdateSchema) -> QuestionGetSchema | None:
        return await self._repository.update(uuid, data)

    async def delete(self, uuid: str) -> QuestionGetSchema | None:
        return await self._repository.delete(uuid)
