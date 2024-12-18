import strawberry

from api.questions.dependencies import get_question_service
from api.questions.types.request import QuestionSchema, QuestionOptionalSchema
from api.questions.types.response import QuestionGetSchema


@strawberry.type
class QuestionMutation:
    @strawberry.mutation
    async def create(
        self,
        schema: QuestionSchema
    ) -> QuestionGetSchema | None:
        return await get_question_service().create(schema)

    @strawberry.mutation
    async def update(
        self,
        uuid: str,
        schema: QuestionOptionalSchema
    ) -> QuestionGetSchema | None:
        return await get_question_service().update(uuid, schema)

    @strawberry.mutation
    async def delete(
        self,
        uuid: str
    ) -> QuestionGetSchema | None:
        return await get_question_service().delete(uuid)
