import sys
import typing

ListItemType = typing.TypeVar('ListItemType')

if sys.version_info > (3, 7):
    class Bool(str): ...  # noqa: E701

    class String(str): ...  # noqa: E701

    class Integer(int): ...  # noqa: E701

    class Float(str): ...  # noqa: E701

    class List(list): ...  # noqa: E701

    class TypedList(typing.Generic[ListItemType], list):
        # TODO: Research run-time check for definitions like thus:
        #  >> numbers = TypedList[int]([1, 2, 3])
        ...  # noqa: E701

if sys.version_info > (3, 8):
    ...

if sys.version_info > (3, 9):
    ...
