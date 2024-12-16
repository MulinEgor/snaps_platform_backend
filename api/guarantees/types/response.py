import strawberry

from api.guarantees.types.request import GuaranteeSchema


@strawberry.type
class GuaranteeGetSchema(GuaranteeSchema):
    uuid: str
