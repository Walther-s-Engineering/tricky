import typing as t

__all__ = (
    'filter_item',
)

Item = t.TypeVar('Item', bound=t.Any)
Iterables = t.Iterable[t.Any]


def filter_item(
    items: Iterables,
    condition: t.Callable[..., bool],
    default: t.Optional[Item] = None,
) -> t.Any:
    return next(
        (item for item in items if condition(item) is True),
        default,
    )
