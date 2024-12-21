import strawberry


@strawberry.input
class RoleCreateSchema:
    name: str


@strawberry.type
class RoleGetSchema(RoleCreateSchema):
    uuid: str
