import strawberry
from typing import Optional


@strawberry.input
class QuestionSchema:
    question: str
    answer: str


@strawberry.input
class QuestionOptionalSchema:
    question: Optional[str] = None
    answer: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            key: value
            for key, value in self.__dict__.items()
            if value is not None
        }
