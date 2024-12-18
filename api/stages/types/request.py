import strawberry
from typing import Optional


@strawberry.input
class StageSchema:
    place: int
    name: str
    description: str


@strawberry.input
class StageOptionalSchema:
    place: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            key: value
            for key, value in self.__dict__.items()
            if value is not None
        }
