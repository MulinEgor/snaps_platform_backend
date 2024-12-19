import strawberry
from prisma.enums import ApplicationType

from api.schemas import DictMixin, OptionalSchemaMeta


@strawberry.input
class FavorCreateSchema:
    name: str
    includes: list[str]
    duration_weeks: float = None
    price: float
    application_type: ApplicationType


@strawberry.input
class FavorUpdateSchema(FavorCreateSchema, DictMixin, metaclass=OptionalSchemaMeta):
    pass


@strawberry.type
class FavorGetSchema(FavorCreateSchema):
    uuid: str
