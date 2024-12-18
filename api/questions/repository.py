from prisma.models import Question

from api.questions.types.request import QuestionSchema, QuestionOptionalSchema
from api.repository import Repository


class QuestionRepository(Repository):
    def __init__(self):
        super().__init__('question')

    async def get(self, uuid: str) -> Question | None:
        return await super().get(uuid)

    async def get_all(self, filters: QuestionOptionalSchema) -> list[Question] | None:
        return await super().get_all(filters.to_dict())

    async def create(self, data: QuestionSchema) -> Question:
        return await super().create(data.__dict__)

    async def update(self, uuid: str, data: QuestionOptionalSchema) -> Question:
        return await super().update(uuid, data.to_dict())

    async def delete(self, uuid: str) -> Question:
        return await super().delete(uuid)
