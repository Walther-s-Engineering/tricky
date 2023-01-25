import typing as t

from pydantic.validators import str_validator
from tricky.typing import String

__all__ = (
    'CommaSeparatedString',
)

CallableGenerator = t.Generator[t.Callable[..., t.Any], None, None]


class CommaSeparatedString(String):
    @classmethod
    def __modify_schema__(cls, field_schema: t.Dict[String, t.Any]) -> None:
        pass

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield str_validator
        yield cls.validate

    @classmethod
    def validate(cls, value: t.Union[String]) -> t.List[String]:
        return list(String(val.strip().strip('"')) for val in value.split(','))
