import strawberry
from typing import Optional
import prisma


@strawberry.input
class FavorCreateSchema:
    name: str
    includes: list[str]
    duration_weeks: float
    price: float
    application_type: prisma.models.enums.ApplicationType


@strawberry.input
class FavorOptionalSchema:
    name: Optional[str] = None
    includes: Optional[list[str]] = None
    duration_weeks: Optional[float] = None
    price: Optional[float] = None
    application_type: Optional[prisma.models.enums.ApplicationType] = None

    def to_dict(self) -> dict:
        return {
            key: value
            for key, value in self.__dict__.items()
            if value is not None
        }
