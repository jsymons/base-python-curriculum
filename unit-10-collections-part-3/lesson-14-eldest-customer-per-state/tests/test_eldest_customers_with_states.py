def test_eldest_customers_with_states():
    """Should return the eldest customer per state."""
    customers = {
        'UT': [{
            'name': 'Mary',
            'age': 28
        }, {
            'name': 'John',
            'age': 31
        }, {
            'name': 'Robert',
            'age': 16
        }],
        'NY': [{
            'name': 'Linda',
            'age': 71
        }, {
            'name': 'Lisa',
            'age': 25
        }, {
            'name': 'Daniel',
            'age': 45
        }],
        'CA': [{
            'name': 'Barbara',
            'age': 15
        }, {
            'name': 'Paul',
            'age': 18
        }, {
            'name': 'Helen',
            'age': 29
        }]
    }
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
    assert eldest_customer_per_state(customers) == expected_result
