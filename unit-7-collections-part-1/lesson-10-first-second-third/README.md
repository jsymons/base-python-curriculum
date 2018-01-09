# First - Second - Third - Last

The function `insert_human` receives a list, a position and an element to insert (similar to the `insert` method). The difference is that the position is specified in a "human" manner. Examples:

```python
list_1 = ['a', 'b', 'c']

insert_human(list_1, 'first', 'Z')
print(list_1)  # ['Z', 'a', 'b', 'c']

list_2 = ['a', 'b', 'c']

insert_human(list_2, 'second', 'Z')
print(list_2)  # ['a', 'Z','b', 'c']

list_3 = ['a', 'b', 'c']

insert_human(list_3, 'last', 'Z')
print(list_3)  # ['a','b', 'c', 'Z']
```
