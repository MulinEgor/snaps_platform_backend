import strawberry

from api.questions.dependencies import get_question_service
from api.questions.schemas import QuestionUpdateSchema, QuestionGetSchema


@strawberry.type
class QuestionQuery:
    @strawberry.field
    async def questions(
        self,
        filters: QuestionUpdateSchema
    ) -> list[QuestionGetSchema]:
        return await get_question_service().get_all(filters)
