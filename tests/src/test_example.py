import pytest


class TestExample:
    @pytest.fixture
    def example_fixture(self) -> bool:
        return True

    def test_example(self, example_fixture: bool) -> None:
        assert True
        assert example_fixture is True
