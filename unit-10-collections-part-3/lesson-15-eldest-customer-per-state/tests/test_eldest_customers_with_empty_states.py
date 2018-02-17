def test_eldest_customers_with_empty_states():
    customers = {
        'UT': [{
            'name': 'Mary',
            'age': 28
        }, {
            'name': 'John',
            'age': 31
        }],
        'NY': []
    }
    expected_result = {
        'UT': {
            'name': 'John',
            'age': 31
        },
        'NY': None
    }
    assert eldest_customer_per_state(customers) == expected_result
