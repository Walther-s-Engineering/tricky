import typing as t

from tricky.utils.decorators import suppress


class TestDecorators:
    class TestSupressDecorator:
        def test_supress_with_builtin_exc(
            self,
            not_raises: t.Callable[..., t.ContextManager[Exception]],
        ) -> None:
            exceptions = [
                AssertionError,
                AttributeError,
                ZeroDivisionError,
                Exception,
                EnvironmentError,
            ]
            for exception in exceptions:
                @suppress(None, (exception,))
                def testing_function() -> t.NoReturn:
                    raise exception()

                with not_raises(exception):
                    result = testing_function()

                assert result is None

        def test_supress_custom_exception_type(
            self,
            not_raises: t.Callable[..., t.ContextManager[Exception]],
        ) -> None:
            class SomeCustomException(Exception):
                pass

            @suppress(None, (SomeCustomException,))
            def testing_function() -> t.NoReturn:
                raise SomeCustomException()

            with not_raises(SomeCustomException):
                result = testing_function()

            assert result is None

        def test_supress_returns_valid_default_value(
            self,
            not_raises: t.Callable[..., t.ContextManager[Exception]],
        ) -> None:
            defaults = [
                1,
                1.5,
                True,
                False,
                'String',
                b'ByteString',
                dict(),
                set(),
                tuple(),
            ]
            for default_value in defaults:
                @suppress(default_value, (Exception,))
                def testing_function():
                    raise Exception()

                with not_raises(Exception):
                    result = testing_function()

                assert result == default_value
