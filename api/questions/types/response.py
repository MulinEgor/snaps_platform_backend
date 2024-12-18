import strawberry

from api.questions.types.request import QuestionSchema


@strawberry.type
class QuestionGetSchema(QuestionSchema):
    uuid: str
