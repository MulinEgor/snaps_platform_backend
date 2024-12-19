import strawberry

from api.schemas import DictMixin, OptionalSchemaMeta


@strawberry.input
class GuaranteeCreateSchema:
    name: str
    image_url: str


@strawberry.input
class GuaranteeUpdateSchema(GuaranteeCreateSchema, DictMixin, metaclass=OptionalSchemaMeta):
    pass


@strawberry.type
class GuaranteeGetSchema(GuaranteeCreateSchema):
    uuid: str
