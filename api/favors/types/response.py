import strawberry

from api.favors.types.request import FavorSchema


@strawberry.type
class FavorGetSchema(FavorSchema):
    uuid: str
