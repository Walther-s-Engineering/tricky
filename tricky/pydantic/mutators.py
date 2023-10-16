import copy
import sys

from typing import TypeVar

from pydantic.main import BaseModel
from tricky.typing import Bool

AnyObject = TypeVar('AnyObject', bound=BaseModel)
AnyObjectAttributes = TypeVar('AnyObjectAttributes')


if sys.version_info > 3.7:
    def mutate(
        object_to_mutate: AnyObject,
        mutate_origin: Bool = False,
        **attrs: AnyObjectAttributes,
    ) -> AnyObject:
        if hasattr(object_to_mutate, '__dict__') is False:
            raise AttributeError(
                'Object cannot be mutate due not implements \'__dict__\' attribute',
            )
        if isinstance(mutate_origin, bool) is False:
            raise TypeError(f'Argument \'mutate_origin\' must be a type of \'{Bool}\'')

        if mutate_origin is True:
            mutating_object: AnyObject = object_to_mutate
        else:
            mutating_object: AnyObject = copy.deepcopy(object_to_mutate)

        mutating_object.__dict__.update(attrs)
        return mutating_object


if sys.version_info > (3, 9):
    def mutate(
        object_to_mutate: AnyObject,
        mutate_origin: Bool = False,
        **attrs: AnyObjectAttributes,
    ) -> AnyObject:
        if hasattr(object_to_mutate, '__dict__') is False:
            raise AttributeError(
                'Object cannot be mutate due not implements \'__dict__\' attribute',
            )
        match mutate_origin:
            case True:
                mutating_object: AnyObject = object_to_mutate
            case False:
                mutating_object: AnyObject = copy.deepcopy(object_to_mutate)
            case _:
                raise TypeError(f'Argument \'mutate_origin\' must be a type of \'{Bool}\'')
        mutating_object.__dict__.update(attrs)
        return mutating_object
