from __future__ import annotations

import functools
import copy
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

_TypedListItem = t.TypeVar('_TypedListItem')
_TypedListItemType = t.TypeVar('_TypedListItemType')
_ConcreteString = t.TypeVar('_ConcreteString')


class _StringValidationTransferObject(t.NamedTuple):
    annotated_type: Type
    annotated_value: t.Any
    origin_new: t.Callable[..., ...]


if sys.version_info > (3, 7):
    Bool: te.TypeAlias = bool
    String: te.TypeAlias = str
    Integer: te.TypeAlias = int
    Float: te.TypeAlias = float
    List: te.TypeAlias = list
    Tuple: te.TypeAlias = tuple
    Type: te.TypeAlias = type

    # TODO: Make thread-safe
    class AnnotatedString(t.Generic[_ConcreteString], String):
        __annotated_value: String

        def __init__(self, _: String) -> None:
            super().__init__()

        def __new__(cls, *args, **kwargs) -> AnnotatedString:
            if args:
                validator: _StringValidationTransferObject = args[0]
                passed_value: String = args[1]
            else:
                raise ValueError(f'The passed value cannot be of type  {type(None)}')

            if passed_value is not None:
                if passed_value != validator.annotated_value:
                    raise ValueError(
                        f'Annotated and passed values are not equal '
                        f'\'{validator.annotated_value}\' != \'{passed_value}\''
                    )
            cls.__new__ = validator.origin_new
            instance = super().__new__(cls, passed_value)
            return instance

        def __class_getitem__(cls, item: String) -> t.Type[AnnotatedString]:
            if isinstance(item, String) is True:
                origin_new = copy.deepcopy(cls.__new__)
                cls.__new__ = functools.partialmethod(
                    cls.__new__,
                    _StringValidationTransferObject(
                        annotated_type=String,
                        annotated_value=item,
                        origin_new=origin_new,
                    ),
                )
                return cls
            raise TypeError(
                f'The annotated value must be type of {String}, '
                f'not {type(item)}',
            )


    # TODO: Make thread-safe
    class TypedList(t.Generic[_TypedListItemType], List):
        __annotated_type: Type

        def __init__(self, *sequence) -> None:
            super().__init__(sequence)

        def __new__(cls, *sequence: t.Tuple[_TypedListItem]) -> TypedList[_TypedListItemType]:
            for item in sequence:
                if isinstance(item, cls.__annotated_type) is False:
                    raise ValueError(
                        f'The passed item "{item}" of the sequence is of type {type(item)}, '
                        f'but the annotated type is {cls.__annotated_type}',
                    )

            if isinstance(sequence, tuple) is True:
                instance = super().__new__(cls)
                return instance
            else:
                raise ValueError(sequence)

        def __class_getitem__(cls, type_: Type) -> t.Type[TypedList]:
            if isinstance(type_, Type) is True:
                cls.__annotated_type = type_
                return cls
            raise TypeError(f'The annotated value must be a type, not {type(type_)}')


if sys.version_info > (3, 8):
    Bool: te.TypeAlias = bool
    String: te.TypeAlias = str
    Integer: te.TypeAlias = int
    Float: te.TypeAlias = float
    List: te.TypeAlias = list
    Tuple: te.TypeAlias = tuple
    Type: te.TypeAlias = type


if sys.version_info > (3, 9):
    Bool: te.TypeAlias = bool
    String: te.TypeAlias = str
    Integer: te.TypeAlias = int
    Float: te.TypeAlias = float
    List: te.TypeAlias = list
    Tuple: te.TypeAlias = tuple
    Type: te.TypeAlias = type


if sys.version_info > (3, 10):
    Bool: t.TypeAlias = bool
    Bytes: t.TypeAlias = bytes
    BytesArray: t.TypeAlias = bytearray
    Dict: t.TypeAlias = dict
    String: t.TypeAlias = str
    Integer: t.TypeAlias = int
    Float: t.TypeAlias = float
    List: t.TypeAlias = list
    Type: t.TypeAlias = type
