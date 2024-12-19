import strawberry

from api.schemas import DictMixin, OptionalSchemaMeta


@strawberry.input
class StageCreateSchema:
    place: int
    name: str
    description: str


@strawberry.input
class StageUpdateSchema(StageCreateSchema, DictMixin, metaclass=OptionalSchemaMeta):
    pass


@strawberry.type
class StageGetSchema(StageCreateSchema):
    uuid: str
