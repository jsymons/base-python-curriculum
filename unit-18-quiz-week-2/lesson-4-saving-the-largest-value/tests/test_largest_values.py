def test_largest_values():
    d1 = {
        'a': 30,
        'b': 10,
        'c': 5
    }

    d2 = {
        'a': 7,
        'b': 'hi',
        'c': 90
    }

    d3 = {
        'a': 'aloha',
        'b': 'howdy',
        'c': 'hello'
    }

    result = {
        'd1': 30,
        'd2': 90,
        'd3': None
    }

    assert get_largest_numbers(d1, d2, d3) == result