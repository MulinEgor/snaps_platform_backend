import strawberry
from typing import Optional
from prisma.enums import ApplicationType

from api.schemas import DictMixin, OptionalSchemaMeta


@strawberry.input
class ReviewCreateSchema:
    name: str
    description: str
    reviewer_name: str


@strawberry.input
class ReviewUpdateSchema(ReviewCreateSchema, DictMixin, metaclass=OptionalSchemaMeta):
    pass


@strawberry.input
class ProjectCreateSchema:
    name: str
    description: str
    application_type: ApplicationType
    duration_weeks: float
    image_urls: list[str]
    review: Optional[ReviewCreateSchema] = None


@strawberry.input
class ProjectUpdateSchema(ProjectCreateSchema, DictMixin, metaclass=OptionalSchemaMeta):
    pass


@strawberry.type
class ReviewGetSchema(ReviewCreateSchema):
    uuid: str


@strawberry.type
class ProjectGetSchema(ProjectCreateSchema):
    uuid: str
    review: Optional[ReviewGetSchema] = None
