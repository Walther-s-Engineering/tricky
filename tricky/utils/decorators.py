import contextlib
import functools
import inspect
import typing as t

DefaultAny = t.TypeVar('DefaultAny')


def suppress(default_value, exceptions: t.Tuple[t.Type[Exception]] = (Exception,)):
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
