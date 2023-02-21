# tricky - that's about python.

This module is simply a collection of useful code, utilities, and functions to simplify your work with the language and the tasks you solve.

## Collection:
1. Iterables module `tricky.iterables`
2. Typing `tricky.typing` (wip)


## Examples:

### Iterables
1. Example of **iterables.filter_item**
 ```python
 from tricky.iterables import filter_item
 
 numbers = range(1000)
 result: int = filter_item(
     numbers,  # the iterable
     lambda number: number == 342,  # condition to get your item
     None,  # the default value to return, if condition not met
 )
 print(result)
 # 342
 ```

### Typing

1. An example of a simple use of a **TypedList**:
```python
from tricky.typing import TypedList

numbers = TypedList[int](1, 2, 3, 4, 5)
assert isinstance(numbers, (list, TypedList))  # True
```

But if an element with a different type is passed to the list, an exception will be thrown:
```python
from tricky.typing import TypedList

numbers = TypedList[int](1, 2, 3, 'string', 5)
# ValueError: Passed item "string" of sequence has type <class 'str'>, but annotated type is <class 'int'>
```

2. An example of a simple use of a **AnnotatedString**
```python
from tricky.typing import AnnotatedString

expecting_value = 'example'
annotated_string = AnnotatedString['example'](expecting_value)
assert isinstance(AnnotatedString['example'](expecting_value), (str, AnnotatedString))
```
But if the annotated value does not match the one passed, an exception will be thrown
```python
from tricky.typing import AnnotatedString

bad_value = 'bad_value'
annotated_string = AnnotatedString['example'](bad_value)
# ValueError: Annotated and passed values are not equal 'bad_value' != 'example'
```
