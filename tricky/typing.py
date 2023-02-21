from __future__ import annotations

import sys
import typing as t
import typing_extensions as te

__all__ = (
    'Bool',
    'String',
    'Integer',
    'Float',
    'List',
    'TypedList',
    'AnnotatedString',
)

ListItemType = t.TypeVar('ListItemType')
ConcreteString = t.TypeVar('ConcreteString')


if sys.version_info > (3, 7):
    Bool: te.TypeAlias = bool
    String: te.TypeAlias = str
    Integer: te.TypeAlias = int
    Float: te.TypeAlias = float
    List: te.TypeAlias = list
    Tuple: te.TypeAlias = tuple

    class AnnotatedString(t.Generic[ConcreteString], String):
        __annotated_value: str

        def __init__(self, _: str) -> None:
            super().__init__()

        def __new__(cls, *args, **kwargs) -> AnnotatedString:
            if args:
                passed_value = args[0]
            else:
                raise ValueError(f'The passed value cannot be of type  {type(None)}')
            if passed_value is not None:
                if passed_value != cls.__annotated_value:
                    raise ValueError(
                        f'Annotated and passed values are not equal '
                        f'\'{passed_value}\' != \'{cls.__annotated_value}\''
                    )
            instance = super().__new__(cls)
            return instance

        def __class_getitem__(cls, item: String) -> t.Type[AnnotatedString]:
            if isinstance(item, String) is True:
                cls.__annotated_value = item
                return cls
            raise TypeError(
                f'The annotated value must be type of {String}, '
                f'not {type(item)}',
            )

    _TypeAnnotation = t.TypeVar('_TypeAnnotation')

    class TypedList(t.Generic[ListItemType], List):
        __annotated_type: type

        def __init__(self, *sequence) -> None:
            super().__init__(sequence)

        def __new__(cls, *sequence: Tuple[t.Any]) -> TypedList:
            for item in sequence:
                if isinstance(item, cls.__annotated_type) is False:
                    raise ValueError(
                        f'The passed item "{item}" of the sequence is of type {type(item)}, '
                        f'but the annotated type is {cls.__annotated_type}',
                    )

            if isinstance(sequence, Tuple) is True:
                instance = super().__new__(cls, sequence)
                return instance
            else:
                raise ValueError(sequence)

        def __class_getitem__(cls, type_: _TypeAnnotation) -> t.Type[TypedList]:
            if isinstance(type_, type) is True:
                cls.__annotated_type = type_
                return cls
            raise TypeError(f'The annotated value must be a type, not {type(type_)}')

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
