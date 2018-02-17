def test_add_book_to_purchase_base_use_case():
    purchase = {
        'id': 99,
        'books': [{
            'title': 'The Raven',
            'author': 'Edgar Allan Poe',
            'price': 19.99
        }, {
            'title': 'Ulysses',
            'author': 'James Joyce',
            'price': 23.99
        }],
        'total': 0
    }

    add_book_to_purchase(
        purchase,
        title='The Odyssey',
        author='Homer',
        price=7.99)

    assert len(purchase['books']) == 3
    assert purchase['books'] == [{
        'title': 'The Raven',
        'author': 'Edgar Allan Poe',
        'price': 19.99
    }, {
        'title': 'Ulysses',
        'author': 'James Joyce',
        'price': 23.99
    }, {
        'title': 'The Odyssey',
        'author': 'Homer',
        'price': 7.99
    }]