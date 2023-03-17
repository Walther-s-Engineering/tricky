import typing as t

from datetime import datetime, timezone

from pydantic.validators import str_validator
from pydantic.datetime_parse import parse_datetime

from tricky.typing import String

__all__ = (
    'CommaSeparatedStringField',
)

CallableGenerator = t.Generator[t.Callable[..., t.Any], None, None]


class CommaSeparatedStringField(String):
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


class UTCDatetimeField(datetime):
    @classmethod
    def __modify_schema__(cls, field_schema: t.Dict[String, t.Any]):
        pass

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield parse_datetime
        yield cls.ensure_tzinfo
        yield cls.validate

    @classmethod
    def ensure_tzinfo(cls, value: datetime) -> datetime:
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc)

    @staticmethod
    def validate(date_time: datetime) -> String:
        return date_time.isoformat()
