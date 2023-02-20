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
    Bool = bool
    Bytes = bytes
    BytesArray = bytearray
    Dict = dict
    String = str
    Integer = int
    Float = float
    List = list

if sys.version_info > (3, 9):
    Bool = bool
    Bytes = bytes
    BytesArray = bytearray
    Dict = dict
    String = str
    Integer = int
    Float = float
    List = list

if sys.version_info > (3, 10):
    Bool: t.TypeAlias = bool
    Bytes: t.TypeAlias = bytes
    BytesArray: t.TypeAlias = bytearray
    Dict: t.TypeAlias = dict
    String: t.TypeAlias = str
    Integer: t.TypeAlias = int
    Float: t.TypeAlias = float
    List: t.TypeAlias = list
