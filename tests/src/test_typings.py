import typing as t

import pytest

from tricky.typing import AnnotatedString


class TestTypings:
    def test_typed_string(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        expecting = 'some_string'
        with not_raises(ValueError, TypeError):
            string = AnnotatedString['some_string'](expecting)

        assert string == expecting
        assert isinstance(string, (str, AnnotatedString))

    def test_typed_string_raises_value_error(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        expecting = 'some_string'
        with pytest.raises(ValueError):
            _ = AnnotatedString['wrong_string'](expecting)

    def test_typed_string_raises_type_error(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        expecting = 'some_string'
        with pytest.raises(TypeError):
            _ = AnnotatedString[100](expecting)

    def test_typed_string_values_no_conflicts(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        expecting_one = 'first_expectation'
        expecting_two = 'second_expectation'

        with not_raises(ValueError):
            string_one = AnnotatedString[expecting_one](expecting_one)
            string_two = AnnotatedString[expecting_two](expecting_two)

            assert string_one != expecting_two
            assert string_two != expecting_one
