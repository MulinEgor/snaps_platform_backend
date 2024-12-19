import strawberry

from api.questions.dependencies import get_question_service
from api.questions.schemas import QuestionCreateSchema, QuestionUpdateSchema, QuestionGetSchema


@strawberry.type
class QuestionMutation:
    @strawberry.mutation
    async def create(
        self,
        schema: QuestionCreateSchema
    ) -> QuestionGetSchema | None:
        return await get_question_service().create(schema)

    @strawberry.mutation
    async def update(
        self,
        uuid: str,
        schema: QuestionUpdateSchema
    ) -> QuestionGetSchema | None:
        return await get_question_service().update(uuid, schema)

    @strawberry.mutation
    async def delete(
        self,
        uuid: str
    ) -> QuestionGetSchema | None:
        return await get_question_service().delete(uuid)
