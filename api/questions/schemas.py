import strawberry

from api.schemas import DictMixin, OptionalSchemaMeta


@strawberry.input
class QuestionCreateSchema:
    question: str
    answer: str


@strawberry.input
class QuestionUpdateSchema(QuestionCreateSchema, DictMixin, metaclass=OptionalSchemaMeta):
    pass


@strawberry.type
class QuestionGetSchema(QuestionCreateSchema):
    uuid: str
