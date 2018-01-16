def test_invert_one_element_dict():
    assert invert_dict({1: 'a'}) == {'a': 1}
