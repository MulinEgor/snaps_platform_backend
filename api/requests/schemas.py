import strawberry
from prisma.enums import ApplicationType, Status

from api.schemas import DictMixin, OptionalSchemaMeta


@strawberry.input
class RequestCreateSchema:
    name: str
    email: str
    phone: str
    application_type: ApplicationType
    description: str
    price: float


@strawberry.input
class RequestUpdateSchema(RequestCreateSchema, DictMixin, metaclass=OptionalSchemaMeta):
    pass


@strawberry.type
class RequestGetSchema(RequestCreateSchema):
    uuid: str
    status: Status
