# Add book to purchase

Write a function `add_book_to_purchase` that receives a dictionary with purchase information and adds a book to the given purchase dict. Each purchase dict has a key `books` that contains a list of books. Your job is to append the book to that list.

Example:

```python
purchase = {
    'id': 99,
    'books': [],  # Empty list of books
    'total': 0
}
add_book_to_purchase(
    purchase,
    title='The Odyssey',
    author='Homer',
    price=7.99)
print(purchase)
```

Prints: 

```python
{
    'id': 99,
    'books': [{
        'title': 'The Odyssey',
        'author': 'Homer',
        'price': 7.99
    }],  # The list of books has one book
    'total': 0
}
```
