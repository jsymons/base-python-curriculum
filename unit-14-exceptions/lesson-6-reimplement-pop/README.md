# Reimplement Pop

Sometimes the best ways to get better at coding is to try and recreate features that already exist on your own.

In this exercise, the goal is to replicate the functionality of the dictionary `pop` method. Write a function `pop` that receives a `dictionary`, a `key`, and an optional parameter `default_value` that is set to `None` by default.

Using a `try/except` clause, try and delete the key-value pair in the `dictionary`, returning the value of the key-value pair if it is successfully deleted. If the key is not found and there is a `default_value`, return `default_value`. Otherwise, raise a KeyError.

Examples:

```python
test_dict = {
    "cat": "hat",
    "dog": "log",
    "elf": "shelf"
}

pop(test_dict, "dog") # "log"

# Resulting test_dict
test_dict = {
    "cat": "hat",
    "elf": "shelf"
}

# "horse" key not in dictionary so returns default_value
pop(test_dict, "horse", "crickets") # "crickets"

# "horse" key not in dictionary and no default value so KeyError
pop(test_dict, "horse") # Raises KeyError
```