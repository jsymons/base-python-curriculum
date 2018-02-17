def test_number_of_customers_per_state_with_blank_state():
    """Should return the correct number of customers per state."""
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
        'NY': None,  # Be Careful! NY value is None
        'CA': [{
            'name': 'Barbara',
            'age': 15
        }, {
            'name': 'Paul',
            'age': 18
        }]
    }
    expected_result = {
        'UT': 3,
        'NY': 0,
        'CA': 2
    }
    assert number_of_customers_per_state(customers) == expected_result
