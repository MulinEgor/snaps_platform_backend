import strawberry
from typing import Optional


@strawberry.input
class TeamMemberSchema:
    name: str
    position: str
    description: str
    image_url: str


@strawberry.input
class TeamMemberOptionalSchema:
    name: Optional[str] = None
    position: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            key: value
            for key, value in self.__dict__.items()
            if value is not None
        }
