import typing as t

from .typing import Bool

__all__ = (
    'filter_item',
    'remove_values_from_iterable',
)

Item = t.TypeVar('Item', bound=t.Any)
Iterables = t.Iterable[t.Any]


def filter_item(
    items: Iterables,
    condition: t.Callable[..., t.Union[Bool, bool]],
    default: t.Optional[Item] = None,
) -> t.Any:
    return next(
        (item for item in items if condition(item) is True),
        default,
    )


def remove_values_from_iterable(
    initial_values: t.Iterable[t.Any],
    values_to_remove: t.Iterable[t.Any],
) -> t.List[t.Any]:
    return [
        initial_value
        for initial_value in initial_values
        if initial_value not in values_to_remove
    ]
