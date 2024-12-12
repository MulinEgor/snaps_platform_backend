import strawberry
from typing import Optional


@strawberry.input
class FavorCreateSchema:
    name: str
    includes: str
    duration_weeks: float
    price: float


@strawberry.input
class FavorUpdateSchema:
    name: Optional[str] = None
    includes: Optional[str] = None
    duration_weeks: Optional[float] = None
    price: Optional[float] = None

    def to_dict(self) -> dict:
        return {
            key: value
            for key, value in self.__dict__.items()
            if value is not None
        }
