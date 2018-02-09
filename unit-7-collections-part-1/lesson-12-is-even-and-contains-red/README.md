# Is even and contains red

Write a function `is_even_and_contains_red` that receives a list (containing colors) and returns True if the list contains the color `"red"` **AND** has an even number of elements. False, otherwise. Check the examples:

```python
# 4 elements (even) with red:
is_even_and_contains_red(['red', 'blue', 'green', 'white'])  # True

# 3 elements (odd!) with red:
is_even_and_contains_red(['red', 'blue', 'green'])  # False

# 2 elements (even!) **WITHOUT** red:
is_even_and_contains_red(['white', 'blue', 'green', 'black'])  # False

# 3 elements (odd!) **WITHOUT** red:
is_even_and_contains_red(['white', 'blue', 'green'])  # False
```
