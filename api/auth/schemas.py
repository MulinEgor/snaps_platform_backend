import strawberry

from api.auth.jwt.schemas import JWTGetSchema
from api.auth.users.schemas import UserGetSchema


@strawberry.type
class AuthGetSchema:
    user: UserGetSchema
    tokens: JWTGetSchema
