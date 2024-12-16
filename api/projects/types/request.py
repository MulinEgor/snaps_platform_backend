import strawberry
from typing import Optional
from prisma.enums import ApplicationType


@strawberry.input
class ReviewSchema:
    name: str
    description: str
    reviewer_name: str


@strawberry.input
class ProjectSchema:
    name: str
    description: str
    application_type: ApplicationType
    duration_weeks: float
    image_urls: list[str]
    review: Optional[ReviewSchema] = None


@strawberry.input
class ProjectOptionalSchema:
    name: Optional[str] = None
    description: Optional[str] = None
    application_type: Optional[ApplicationType] = None
    duration_weeks: Optional[float] = None
    image_urls: Optional[list[str]] = None
    review: Optional[ReviewSchema] = None

    def to_dict(self) -> dict:
        return {
            key: value
            for key, value in self.__dict__.items()
            if value is not None
        }
