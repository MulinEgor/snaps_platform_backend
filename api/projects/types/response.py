from typing import Optional
import strawberry

from api.projects.types.request import ProjectSchema, ReviewSchema


@strawberry.type
class ReviewGetSchema(ReviewSchema):
    uuid: str


@strawberry.type
class ProjectGetSchema(ProjectSchema):
    uuid: str
    review: Optional[ReviewGetSchema] = None
