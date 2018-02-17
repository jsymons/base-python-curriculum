# Eldest customer per state

With the same structure as before, now you need to write a function that finds the eldest customer per state. Example:

```python
customers = {
    'UT': [{
        'name': 'Mary',
        'age': 28
    }, {
        'name': 'John',  # Eldest
        'age': 31
    }, {
        'name': 'Robert',
        'age': 16
    }],
    'NY': [{
        'name': 'Linda',  # Eldest (only customer)
        'age': 71
    }],
    'CA': [{
        'name': 'Barbara',
        'age': 15
    }, {
        'name': 'Paul',
        'age': 18
    }, {
        'name': 'Helen',  # Eldest
        'age': 29
    }]
}
results = eldest_customer_per_state(customers)
print(results)
```

Prints:

```python
expected_result = {
    'UT': {
        'name': 'John',
        'age': 31
    },
    'NY': {
        'name': 'Linda',
        'age': 71
    },
    'CA': {
        'name': 'Helen',
        'age': 29
    }
}
```
