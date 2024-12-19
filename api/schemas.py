from typing import Optional


class OptionalSchemaMeta(type):
    def __new__(cls, name, bases, attrs):
        if not attrs.get('__annotations__'):
            attrs['__annotations__'] = {}
        for base in bases:
            if hasattr(base, '__annotations__'):
                for base_key, base_value in base.__annotations__.items():
                    if base_key not in attrs:
                        attrs['__annotations__'][base_key] = Optional[base_value]
        for key in attrs.get('__annotations__', {}):
            attrs[key] = None

        return super().__new__(cls, name, bases, attrs)


class DictMixin:
    def to_dict(self) -> dict:
        return {
            key: value
            for key, value in self.__dict__.items()
            if value is not None
        }
