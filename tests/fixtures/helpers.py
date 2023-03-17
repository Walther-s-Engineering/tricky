from __future__ import annotations

import contextlib
import typing as t

import pytest


@pytest.fixture
def not_raises() -> t.Callable[..., t.Generator]:
    @contextlib.contextmanager
    def _not_raises(*exception: Exception | t.Tuple[Exception]) -> t.Generator:
        try:
            yield
        except exception as err:
            raise err
    return _not_raises
