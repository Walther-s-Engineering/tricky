import sys
import typing as t

ListItemType = t.TypeVar('ListItemType')
__all__ = (
    'Bool',
    'String',
    'Integer',
    'Float',
    'List',
    'TypedList',
)

if sys.version_info > (3, 7):
    class Bool(str): ...  # noqa: E701

    class String(str): ...  # noqa: E701

    class Integer(int): ...  # noqa: E701

    class Float(str): ...  # noqa: E701

    class List(list): ...  # noqa: E701

    class TypedList(t.Generic[ListItemType], list):
        # TODO: Research run-time check for definitions like thus:
        #  >> numbers = TypedList[int]([1, 2, 3])
        ...

if sys.version_info > (3, 8):
    ...

if sys.version_info > (3, 9):
    ...
