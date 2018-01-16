# Is Numeric

Write a function `is_numeric` that receives a parameter and returns `True` if it's numeric (it is, an `int` or a `float`). Examples:

```python
is_numeric(10)  # True, it's an int
is_numeric('10')  # False, it's a string

is_numeric(0.1)  # True, it's a float
is_numeric('0.5')  # False, it's a string

is_numeric(True)  # False! It's a boolean, *SEE NOTES BELOW*
is_numeric(False)  # False! It's a boolean, *SEE NOTES BELOW*
```

## Quick note about booleans

Booleans in [python are tricky](https://blog.rmotr.com/those-tricky-python-booleans-2100d5df92c). For example, if you check if `True` (a boolean) "is an instance of `int`" using the `isinstance` function, the answer will be `True`. That means that **booleans are instances of integers**, it's a "subtype". Examples:

```python
# Boolean values are subtypes of ints
isinstance(True, int)  # True
isinstance(False, int)  # True
```

Don't worry too much about this. In these cases **it's recommended to use the `type` function instead**. `type` of a boolean value will return `bool`:

```python
type(True)  # bool
type(False)  # bool
type(10)  # int
type(0.5)  # float
```
