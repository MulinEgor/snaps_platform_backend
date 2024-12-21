from typing import Optional
import strawberry


@strawberry.input
class JWTCreateSchema:
    uuid: str
    role_name: str
    exp: Optional[int] = None


@strawberry.type
class JWTGetSchema:
    access_token: str
    refresh_token: str
