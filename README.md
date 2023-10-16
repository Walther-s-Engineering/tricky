# tricky - that's not about python.

This Python module named "tricky" is a wonderful collection of handy and versatile utilities designed to assist you in your routine Python programming tasks. With a wide range of convenient functions that operate mostly on iterables and types, your Python experience will become smoother and more efficient.

## Overview

The `tricky` module is mainly composed of:

1. **Iterables Module** (`tricky.iterables`): This sub-module is designed to handle operations and manipulations on iterable objects cleverly.

2. **Typing** (`tricky.typing`): This sub-module provides a more expressive typing system, to deal with items of specific types.


## Examples:

### Iterables

1. Example of **iterables.filter_item**

This function will iterate through a collection of items 
and return the first one that meets the specified condition.
If no such item is found, it will return a default value.

```python
import typing as t
from tricky.typing import Integer
from tricky.iterables import filter_item

numbers = range(1000)
result: t.Optional[Integer] = filter_item(
 numbers,  # the iterable
 lambda number: number == 342,  # condition to get your item
 None,  # the default value to return, if condition not met
)
print(result)
# 342
```

2. **remove_values_from_iterable**
   
This function will create a new list from 'initial_values', excluding any that are in 'values_to_remove'.

```python
import typing as t

from tricky.iterables import remove_values_from_iterable
from tricky.typing import Integer

initial: t.List[Integer] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove: t.List[Integer] = [2, 5, 7]

# We want to remove the numbers 2, 5, and 7 from our initial list.
result = remove_values_from_iterable(initial, remove)

print(result)
# Output: [1, 3, 4, 6, 8, 9, 10]
```

### Typing | tricky.typing

1. An example of a simple use of a **TypedList**:
```python
from tricky.typing import TypedList, Integer

numbers = TypedList[Integer](1, 2, 3, 4, 5)
assert isinstance(numbers, (list, TypedList))  # True
```

But if an element with a different type is passed to the list, an exception will be thrown:
```python
from tricky.typing import TypedList, Integer

numbers = TypedList[Integer](1, 2, 3, 'string', 5)
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
