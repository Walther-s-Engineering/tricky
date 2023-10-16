import contextlib
import functools
import inspect
import typing as t

from types import FunctionType

DefaultAny = t.TypeVar('DefaultAny')
AnyFunction = t.TypeVar('AnyFunction', bound=FunctionType)
DecoratedFunction = t.TypeVar('DecoratedFunction', bound=functools.wraps)


class suppress_and_reraise(contextlib.suppress):
    _exceptions: t.Type[BaseException]

    def __init__(
        self,
        *exceptions: t.Type[BaseException],
        reraise_to: Exception = Exception('Bare re-raised exception'),
    ) -> None:
        super().__init__(*exceptions)
        self._reraise_to = reraise_to

    def __exit__(self, exc_type, exc_val, exc_tb) -> t.NoReturn:
        if exc_type is not None and issubclass(exc_type, self._exceptions):
            raise self._reraise_to


def suppress(default_value, exceptions: t.Tuple[t.Type[Exception], ...] = (Exception,)) -> DecoratedFunction:
    """ This decorator is useful if you need to return the default
    value of a function despite possible errors during its execution.
    """
    def decorating(function):
        if inspect.iscoroutinefunction(function):
            async def wrapper(*args, **kwargs) -> t.Any:
                with contextlib.suppress(*exceptions):
                    return await function(*args, **kwargs)
                return default_value
            return wrapper

        @functools.wraps(function)
        def wrapper(*args, **kwargs) -> t.Any:
            with contextlib.suppress(*exceptions):
                return function(*args, **kwargs)
            return default_value
        return wrapper
    return decorating


def hide_signature(function: AnyFunction) -> AnyFunction:
    """ This decorator is needed to hide the signature of the function being decorated.
    This decorator is useful when working with FastAPI.
    Example:
        ```
        @hide_signature
        def yield_db_session(db_dsn: String) -> Session:
            ...

        def get_items(session: Session = Depends(yield_db_session()): ...
        ```
    """
    function.__wrapped__ = lambda: None
    return function
