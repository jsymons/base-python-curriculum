def test_invert_many_elements_dict():
    assert invert_dict({
        1: 'a', 2: 'b',
        3: 'c', 4: 'd',
        5: 'e'
    }) == {
        'a': 1, 'b': 2,
        'c': 3, 'd': 4,
        'e': 5
    }
