def test_with_many_items():
    result = dict_to_tuple({'Z': 3, 'X': 2, 'Y': 1})
    expected = [('Z', 3), ('X', 2), ('Y', 1)]
    assert sorted(result) == sorted(expected)
