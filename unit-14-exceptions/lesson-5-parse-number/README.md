# Parse Number

If you use the input() function, remember how everything entered is received as a string (regardless of if it was a number or not)?

Write a function `parse_number` to receive a number in string format like '7' and use `try/except` blocks to `try` to change its type into an `int` or a `float`. If that doesn't work, raise a ValueError.

Examples:

```python
parse_number("3") # 3

parse_number("3.2") # 3.2

parse_number("invalid") # Raises ValueError
```