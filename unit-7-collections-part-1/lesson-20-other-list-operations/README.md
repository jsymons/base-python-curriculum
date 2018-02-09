Most important list operations covered during this video:

* `in`
* `len`
* `count`
* `index`

# The `in` operator

Checking if a given element is part of a list is a simple operation that will involve the `in` operator. Let's see an example first:

```python
shopping_list = ['Milk', 'Eggs', 'Bread']

print('Bread' in shopping_list)  # True
print('Cookies' in shopping_list)  # False

do_i_need_to_buy_milk = 'Milk' in shopping_list

print(do_i_need_to_buy_milk)  # True
```

Something to note is that `in` is an **_operator_**, not a function (as `len`, for example) or a list method (like `my_list.remove()` or `my_list.append()`). We use `in` as we'd use other operators (`+`, `-`, etc).
