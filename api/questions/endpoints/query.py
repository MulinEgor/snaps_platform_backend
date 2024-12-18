import strawberry

from api.questions.dependencies import get_question_service
from api.questions.types.request import QuestionOptionalSchema
from api.questions.types.response import QuestionGetSchema


@strawberry.type
class QuestionQuery:
    @strawberry.field
    async def questions(
        self,
        filters: QuestionOptionalSchema
    ) -> list[QuestionGetSchema]:
        return await get_question_service().get_all(filters)
