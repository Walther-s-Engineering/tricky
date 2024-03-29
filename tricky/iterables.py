import contextlib
import typing as t

from .typing import Bool, String

__all__ = (
    'filter_item',
    'remove_values_from_iterable',
    'are_there_duplicates',
    'unpack_values',
    'unpack_values_by_condition',
    'unzip',
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


def are_there_duplicates(sequence: t.Union[t.Iterable, t.Sized]) -> Bool:
    """
    This function are_there_duplicates checks within a sequence if there are any duplicate items.
    It iterates over all elements in the given sequence and for each element,
    it checks if the same element exists in the remaining sequence or not.
    If the element exists, it immediately returns True indicating there are duplicates,
    else if it traversed the entire sequence and found no duplicates, it returns False.

    :param sequence:
    :return: bool:
    """
    # NOTE: This is added because sets in Python are collections of hashable (or immutable)
    #  elements, and dictionaries are mutable, thus not hashable.
    # So, the non-optimized method will be used below.
    with contextlib.suppress(TypeError):
        set_sequence = set(sequence)

        if len(set_sequence) == len(sequence):
            return False
        else:
            return True

    for index, item in enumerate(sequence, start=1):
        if item in sequence[index:]:
            return True
    return False


def unpack_values(
    iterable: t.Iterable[t.Any],
    attribute: String,
) -> t.List[t.Any]:
    return [
        getattr(item, attribute)
        for item in iterable if hasattr(item, attribute)
    ]


def unpack_values_by_condition(
    iterable: t.Iterable[t.Any],
    attribute: String,
    condition: t.Callable[..., t.Any],
) -> t.List[t.Any]:
    return [
        getattr(item, attribute) for item in iterable
        if hasattr(item, attribute) and condition(item) is True
    ]


def unzip(*iterables: t.Iterable[t.Any]) -> t.List[t.Any]:
    return [item for iterable in iterables for item in iterable]
