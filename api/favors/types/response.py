import strawberry

from api.favors.types.request import FavorCreateSchema


@strawberry.type
class FavorGetSchema(FavorCreateSchema):
    uuid: str
