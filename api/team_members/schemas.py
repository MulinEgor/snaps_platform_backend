import strawberry

from api.schemas import DictMixin, OptionalSchemaMeta


@strawberry.input
class TeamMemberCreateSchema:
    name: str
    position: str
    description: str
    image_url: str


@strawberry.input
class TeamMemberUpdateSchema(TeamMemberCreateSchema, DictMixin, metaclass=OptionalSchemaMeta):
    pass


@strawberry.type
class TeamMemberGetSchema(TeamMemberCreateSchema):
    uuid: str
