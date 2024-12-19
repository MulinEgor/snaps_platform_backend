from typing import Optional


class OptionalSchemaMeta(type):
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if isinstance(value, type):
                attrs[key] = Optional[value]
                attrs[key].default = None
        return super().__new__(cls, name, bases, attrs)


class DictMixin:
    def to_dict(self) -> dict:
        return {
            key: value
            for key, value in self.__dict__.items()
            if value is not None
        }
