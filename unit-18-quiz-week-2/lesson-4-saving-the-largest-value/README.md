# Saving the Largest Value

Write a function `get_largest_numbers` that receives 3 dictionaries as parameters: `d1`, `d2`, and `d3`. Get the highest integer value for each dictionary, and return a new dictionary showing the results of each. If there is a non-integer as a value, ignore it. If none of the values are integers, set that result value to None. Your keys in your result dictionary will be the name of each dictionary parameter (hardcoded to "d1", "d2", and "d3").

Example:

Add all the values with the key 'a' together, and you get the sum 22.

```python
d1 = {
    'a': 30,
    'b': 10,
    'c': 5
}

d2 = {
    'a': 7,
    'b': 'hi',
    'c': 90
}

d3 = {
    'a': 'aloha',
    'b': 'howdy',
    'c': 'hello'
}

result = {
    'd1': 30,
    'd2': 90,
    'd3': None
}

sum_of_dict_values(d1, d2, d3) == result