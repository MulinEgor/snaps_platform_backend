import strawberry

from api.stages.types.request import StageSchema


@strawberry.type
class StageGetSchema(StageSchema):
    uuid: str
