import strawberry

from api.auth.utils import requires_admin
from api.questions.dependencies import get_question_service
from api.questions.schemas import QuestionCreateSchema, QuestionUpdateSchema, QuestionGetSchema


@strawberry.type
class QuestionMutation:
    @strawberry.mutation
    @requires_admin
    async def create(
        self,
        info: strawberry.Info,
        schema: QuestionCreateSchema
    ) -> QuestionGetSchema | None:
        return await get_question_service().create(schema)

    @strawberry.mutation
    @requires_admin
    async def update(
        self,
        info: strawberry.Info,
        uuid: str,
        schema: QuestionUpdateSchema
    ) -> QuestionGetSchema | None:
        return await get_question_service().update(uuid, schema)

    @strawberry.mutation
    @requires_admin
    async def delete(
        self,
        info: strawberry.Info,
        uuid: str
    ) -> QuestionGetSchema | None:
        return await get_question_service().delete(uuid)
