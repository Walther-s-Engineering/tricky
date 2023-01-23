import typing as t

from string import ascii_letters

from tricky.iterables import filter_item


class TestIterables:

    class TestFilterItem:
        def test_filter_item_with_numbers(self) -> None:
            numbers = range(1000)
            for expecting_number in numbers:
                result: t.Optional[int] = filter_item(
                    numbers,
                    lambda x: x == expecting_number,
                    None,
                )
                assert result is not None
                assert result == expecting_number

        def test_filter_items_with_strings(self) -> None:
            for expecting_string in ascii_letters:
                result: t.Optional[str] = filter_item(
                    ascii_letters,
                    lambda x: x == expecting_string,
                    None,
                )
                assert result is not None
                assert result == expecting_string

        def test_filter_items_with_bytes(self) -> None:
            for expecting_byte in ascii_letters.encode():
                expecting_string = chr(expecting_byte)
                result: t.Optional[str] = filter_item(
                    ascii_letters,
                    lambda x: x == expecting_string,
                    None,
                )
                assert result is not None
                assert result == expecting_string

        def test_filter_items_with_tuple(self) -> None:
            test_items = [
                tuple(range(1000)),
                tuple(ascii_letters),
                tuple([True, False] * 30),
            ]
            for test_item in test_items:
                for expecting in test_item:
                    result: t.Optional[int] = filter_item(
                        test_item,
                        lambda x: x == expecting,
                        None,
                    )
                    assert result is not None
                    assert result == expecting

        def test_filter_items_return_default_is_none(self) -> None:
            numbers = range(1000)
            expecting_number = 1001
            result: t.Optional[int] = filter_item(
                numbers,
                lambda x: x == expecting_number,
                None,
            )
            assert result is None
            assert result != expecting_number