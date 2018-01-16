# Zip two collections

> **IMPORTANT:** For this assignment you **CAN'T** use the builtin `zip` function.

For this assignment, we'll rewrite the builtin function `zip`, it's going to be called `rmotr_zip`. `rmotr_zip` receives two collections (lists, tuples, doesn't matter) and must "zip" their elements. Zip just means matching elements in the same positions for both collections. A conceptual example of zip:

```python
collection_a = ['A', 'B', 'C', 'D']
collection_b = [ 1 ,  2 ,  3 ,  4 ]

# Zip collection_a and collection_b means:

'A' => 1
'B' => 2
'C' => 3
'D' => 4
```

The result is a list containing tuples for each new pair. Example of the `rmotr_zip` function:

```python

result = rmotr_zip(['A', 'B', 'C'], [1, 2, 3])

# The following formatting doesn't change anything
# It's just for readability purposes
result == [
  ('A', 1),
  ('B', 2),
  ('C', 3),
]

# A few more examples
rmotr_zip([1, 1, 1], [2, 2, 2])  # [(1, 2), (1, 2), (1, 2)]
rmotr_zip(['a', 'b'], [1, 2, 3])  # None! Different number of elements
```
