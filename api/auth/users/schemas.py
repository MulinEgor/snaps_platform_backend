import strawberry

from api.auth.roles.schemas import RoleGetSchema
from api.schemas import DictMixin, OptionalSchemaMeta


@strawberry.input
class UserLoginSchema:
    email: str
    password: str


@strawberry.input
class UserCreateSchema:
    email: str
    password: str
    role_uuid: str


@strawberry.input
class UserUpdateSchema(UserCreateSchema, DictMixin, metaclass=OptionalSchemaMeta):
    pass


@strawberry.type
class UserCreateORMSchema:
    email: str
    hashed_password: str
    role_uuid: str


@strawberry.input
class UserUpdateORMSchema(UserCreateORMSchema, DictMixin, metaclass=OptionalSchemaMeta):
    pass


@strawberry.type
class UserGetSchema:
    uuid: str
    email: str
    role: RoleGetSchema
