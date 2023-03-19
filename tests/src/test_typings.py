import os
import threading
import typing as t

import pytest

from tricky.typing import AnnotatedString, TypedList, Integer


class TestTypingsAnnotatedString:
    def test_annotated_string(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        expecting = 'some_string'
        with not_raises(ValueError):
            string = AnnotatedString['some_string'](expecting)

        assert string == expecting
        assert isinstance(string, (str, AnnotatedString))

    def test_annotated_string_raises_value_error(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        expecting = 'some_string'
        with pytest.raises(ValueError):
            _ = AnnotatedString['wrong_string'](expecting)

    def test_annotated_string_raises_type_error(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        expecting = 'some_string'
        with pytest.raises(TypeError):
            _ = AnnotatedString[100](expecting)

    def test_annotated_string_values_no_conflicts(
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

    def test_annotated_string_values_no_conflicts_in_threads(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        def run_thread(thread_index: Integer) -> None:
            expecting_one = f'first_expectation_{thread_index}'
            expecting_two = f'second_expectation_{thread_index}'

            with not_raises(ValueError):
                string_one = AnnotatedString[expecting_one](expecting_one)
                string_two = AnnotatedString[expecting_two](expecting_two)

                assert string_one != expecting_two
                assert string_two != expecting_one

        cpu_count: Integer = os.cpu_count()
        threads: t.List[threading.Thread] = [
            threading.Thread(
                target=run_thread,
                args=(index,),
                name=f'annotated_str_thread_{index}',
            )
            for index in range(os.cpu_count())
        ]
        assert len(threads) == os.cpu_count()

        for thread in threads:
            thread.start()
            thread.join()


class TestTypingTypedList:
    def test_typed_list(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        expecting: t.List[int] = [1, 2]
        with not_raises(ValueError, TypeError):
            typed_list = TypedList[int](expecting)

        assert typed_list == expecting
        assert isinstance(typed_list, (list, TypedList))

    def test_typed_list_raises_type_error_with_string(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        expecting = 'some_string'
        with pytest.raises(TypeError):
            _ = TypedList[int](expecting)

    def test_typed_list_raises_type_error_with_list_of_strings(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        expecting = 'some_string'
        with pytest.raises(TypeError):
            _ = TypedList[int](expecting)

    def test_annotated_string_values_no_conflicts(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        expecting_one = [1, 2]
        expecting_two = [3, 4]

        with not_raises(ValueError):
            list_one = TypedList[int](expecting_one)
            list_two = TypedList[int](expecting_two)

            assert list_one != expecting_two
            assert list_two != expecting_one

    def test_typed_string_values_no_conflicts_in_threads(
        self,
        not_raises: t.Callable[..., t.ContextManager[Exception]]
    ) -> None:
        def run_thread(thread_index: Integer) -> None:
            expecting_one = [1 + thread_index, 2 + thread_index]
            expecting_two = [3 + thread_index, 4 + thread_index]

            with not_raises(ValueError):
                list_one = TypedList[int](expecting_one)
                list_two = TypedList[int](expecting_two)

                assert list_one != expecting_two
                assert list_two != expecting_one

        threads: t.List[threading.Thread] = [
            threading.Thread(
                target=run_thread,
                args=(index,),
                name=f'typed_list_thread_{index}',
            )
            for index in range(os.cpu_count())
        ]
        assert len(threads) == os.cpu_count()

        for thread in threads:
            thread.start()
            thread.join()
