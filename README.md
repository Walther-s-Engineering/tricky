# tricky - that's about python.

This module is simply a collection of useful code, utilities, and functions to simplify your work with the language and the tasks you solve.

## Collection:
1. Iterables module `tricky.iterables`
2. Typing `tricky.typing` (wip)


## Examples:

1. `tricky.iterables.filter_item`
```python
numbers = range(1000)
result: int = filter_item(
    numbers,  # the iterable
    lambda number: number == 342,  # condition to get your item
    None,  # the default value to return, if condition not met
)
print(result)
# 342
```
