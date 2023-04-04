from __future__ import annotations

import sys
import typing as t
import typing_extensions as te

from contextvars import ContextVar

__all__ = (
    'Bool',
    'Bytes',
    'BytesArray',
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


if sys.version_info > (3, 7):
    Bool: te.TypeAlias = bool
    Bytes: te.TypeAlias = bytes
    BytesArray: te.TypeAlias = bytearray
    String: te.TypeAlias = str
    Integer: te.TypeAlias = int
    Float: te.TypeAlias = float
    List: te.TypeAlias = list
    Tuple: te.TypeAlias = tuple
    Type: te.TypeAlias = type

    _annotated_string_transfer_var = ContextVar('string_annotated_value')

    class AnnotatedString(t.Generic[_ConcreteString], String):
        def __new__(cls, *args, **kwargs) -> AnnotatedString:
            if args:
                __passed_value = args[0]
                __annotated_type = _annotated_string_transfer_var.get()
            else:
                raise TypeError(f'The passed value cannot be of type  {type(None)}')
            if __passed_value is not None:
                if __passed_value != __annotated_type:
                    raise ValueError(
                        f'Annotated and passed values are not equal '
                        f'\'{__annotated_type}\' != \'{__passed_value}\''
                    )
            else:
                pass
            __instance = super().__new__(cls, __passed_value)
            __instance.__annotated_type = __annotated_type
            return __instance

        def __class_getitem__(cls, item: String) -> t.Type[AnnotatedString]:
            if isinstance(item, String) is True:
                _annotated_string_transfer_var.set(item)
                return cls
            raise TypeError(
                f'The annotated value must be type of {String}, '
                f'not {type(item)}',
            )

    _typed_list_transfer_var = ContextVar('typed_list_annotated_value')

    class TypedList(t.Generic[_TypedListItemType], List):
        def __new__(cls, *sequence: _TypedListItem) -> TypedList[_TypedListItemType]:
            __annotated_type: Type = _typed_list_transfer_var.get()

            def _validate(iterable: t.Iterable) -> None:
                for item in iterable:
                    if isinstance(item, (list, tuple, set)) is True:
                        return _validate(item)
                    if isinstance(item, __annotated_type) is False:
                        raise TypeError(
                            f'The passed item "{item}" of the sequence is of type {type(item)}, '
                            f'but the annotated type is {__annotated_type}',
                        )
                    continue
            _validate(sequence)

            if isinstance(sequence, tuple) is True:
                __instance = super().__new__(cls)
                __instance.__annotated_type = __annotated_type
                return __instance
            else:
                raise ValueError(sequence)

        def __class_getitem__(cls, type_: Type) -> t.Type[TypedList]:
            if isinstance(type_, Type) is True:
                _typed_list_transfer_var.set(type_)
                return cls
            raise TypeError(f'The annotated value must be a type, not {type(type_)}')


if sys.version_info > (3, 8):
    Bool: te.TypeAlias = bool
    Bytes: te.TypeAlias = bytes
    BytesArray: te.TypeAlias = bytearray
    String: te.TypeAlias = str
    Integer: te.TypeAlias = int
    Float: te.TypeAlias = float
    List: te.TypeAlias = list
    Tuple: te.TypeAlias = tuple
    Type: te.TypeAlias = type


if sys.version_info > (3, 9):
    Bool: te.TypeAlias = bool
    Bytes: te.TypeAlias = bytes
    BytesArray: te.TypeAlias = bytearray
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
