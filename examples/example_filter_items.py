from tricky.iterables import filter_item

numbers = range(100)
expecting_number = 1
result = filter_item(numbers, lambda number: number == expecting_number, 0)

assert result == expecting_number
