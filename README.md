# tricky - that's about python.

This module is simply a collection of useful code, utilities, and functions to simplify your work with the language and the tasks you solve.

## Collection:
1. Iterables module `tricky.iterables`
2. Typing `tricky.typing` (wip)


## Examples:

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

2. Example of **typing**
    ```python
    from tricky.typing import TypedList
    
    numbers = TypedList[int]([1, 2, 3, 4, 5])
    assert isinstance(numbers, list)  # True
    ```
