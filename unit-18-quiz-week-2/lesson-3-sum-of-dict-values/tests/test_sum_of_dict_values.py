def test_sum_of_dict_values():
    d1 = {
    'a': 10,
    'b': 30,
    'c': 5
    }

    d2 = {
        'a': 7,
        'b': 22,
        'c': 90
    }

    d3 = {
        'a': 5,
        'b': 1,
        'c': 'hello'
    }

    result = {
        'a': 22,
        'b': 53,
        'c': None
    }

    assert sum_of_dict_values(d1, d2, d3) == result