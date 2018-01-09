# Sum if list only contains integers

Define a function `sum_if_list_of_ints` that receives a list and uses a loop
to make sure the list only contains integers. If so, it returns the sum of
the integers. If not, return 'not an int'.

Hint: Use isinstance again to determine the type.

Examples:

```python
>>> sum_if_list_of_ints([1, 2, 3])
6
>>> sum_if_list_of_ints([1, 'a', 3])
'not an int'
>>> sum_if_list_of_ints([])
0
```
