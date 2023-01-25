from tricky.typing import (
    Bool,
    String,
    Integer,
    List,
    TypedList
)

assert isinstance(Bool(True), bool)
assert isinstance(True, Bool)

assert isinstance(Integer(1), int)
assert isinstance(1, Integer)

assert isinstance(String('example'), str)
assert isinstance('example', String)

assert isinstance(List(), list)
assert isinstance(list(), List)

assert isinstance(TypedList[int]([1, 2, 3]), list)
