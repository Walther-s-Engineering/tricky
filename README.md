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

2. Example of  **iterables.remove_values_from_iterable**
   
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

3. Example of **iterables.are_there_duplicates**

This function are_there_duplicates checks within a sequence if there are any duplicate items. 
It iterates over all elements in the given sequence and for each element, 
it checks if the same element exists in the remaining sequence or not. 
If the element exists, it immediately returns True indicating there are duplicates, 
else if it traversed the entire sequence and found no duplicates, it returns False.

```python
import typing as t

from tricky.iterables import are_there_duplicates
from tricky.typing import Integer


has_no_duplicates: t.List[Integer] = [1, 2, 3, 4, 5]
has_duplicates: t.List[Integer] = [1, 2, 1, 4, 5]

print(are_there_duplicates(has_no_duplicates))  # Output: False, as there are no duplicates.
print(are_there_duplicates(has_duplicates))  # Output: True, as 1 is repeated.
```

4. Example of **iterables.unpack_values**

The function unpacks the value of a given attribute from a collection of objects. 
It checks each object if it has the said attribute through hasattr method, and if it does, 
it retrieves the value via getattr method. 
The results are then accumulated in a list, which is the returned output.

```python
import typing as t

from tricky.iterables import unpack_values


class SomeClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

iterable: t.List[SomeClass] = [SomeClass(1, 2), SomeClass(3, 4), SomeClass(5, 6)]
attribute = 'a'  # Attribute to extract
print(unpack_values(iterable, attribute))  # Outputs [1, 3, 5]
```

5. Example of **iterables.unpack_values_by_condition**

The function returns a list of values. 
Each value comes from an object from the iterable parameter, 
and specifically from the attribute of that object corresponding to the attribute parameter.

```python
import typing as t

from tricky.iterables import unpack_values_by_condition
from tricky.typing import Integer


class Simple:
    def __init__(self, value):
        self.some_attr = value

# Create a list of Simple objects, where each object has a value attribute from 1 to 5
objects: t.List[Simple] = [Simple(i) for i in range(1, 6)]

# Lookup attribute
lookup_attribute = 'some_attr'

# Condition that checks if the value attribute of the object is greater than 3
condition = (lambda obj: obj.attribute > 3)

# Use the function to get values greater than 3
values: t.List[Integer] = unpack_values_by_condition(objects, lookup_attribute, condition)

print(values)  # It should output: [4, 5]
```


6. Example of **iterables.unzip**

The unzip function in your code is essentially a flatten function.
Specifically, it takes in an arbitrary number of iterable collections (list, tuple, etc.) 
as arguments, and consolidates all the items in these collections into a single, flat list.

```python
import typing as t

from tricky.iterables import unzip
from tricky.typing import Integer, String

numbers: t.List[Integer] = [1, 2, 3, 4]
string: t.List[String] = ['apple', 'banana', 'cherry']

print(unzip(numbers))  # Output: [1, 2, 3, 4, 'apple', 'banana', 'cherry']
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
