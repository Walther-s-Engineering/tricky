import typing as t

from .typing import Bool, List

__all__ = (
    'filter_item',
    'remove_values_from_iterable',
)

Item = t.TypeVar('Item')
Iterables = t.Iterable[Item]


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
    initial_values: Iterables,
    values_to_remove: Iterables,
) -> t.List[Item]:
    return [
        initial_value
        for initial_value in initial_values
        if initial_value not in values_to_remove
    ]


def are_there_duplicates(sequence: t.Iterable) -> Bool:
    for index, item in enumerate(sequence, start=1):
        if item in sequence[index:]:
            return True
    return False
