# Calculate purchase price

## Base case

Following the same structure from the previous assignment, define a function `calculate_purchase_price` that receives a purchase dictionary and computes the sum of the prices of all the books contained in that `purchase`. The function, by default, should NOT update the value in the `purchase` dict.

Example:

```python
purchase = {
    'id': 99,
    'books': [{
        'title': 'Book A',
        'author': 'Author A',
        'price': 3
    }, {
        'title': 'Book B',
        'author': 'Author B',
        'price': 5
    }],  # Empty list of books
    'total': 0
}

total = calculate_purchase_price(purchase)
print(total)  # 8
print(purchase['total'])  # 0  # Not updated. IMPORTANT #
```

## Update the value in purchase

The `calculate_purchase_price` receives an optional parameter `set_to_dict` (boolean) that, if `True`, should set the total (and update) the purchase. Example:

```python
purchase = {
    'id': 99,
    'books': [{
        'title': 'Book A',
        'author': 'Author A',
        'price': 3
    }, {
        'title': 'Book B',
        'author': 'Author B',
        'price': 5
    }],  # Empty list of books
    'total': 0
}

total = calculate_purchase_price(purchase, set_to_dict=True)
print(total)  # 8  # Value is returned, normally
# but it's also set in the purchase
print(purchase['total'])  # 8
```
