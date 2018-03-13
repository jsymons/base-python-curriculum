def test_tuple_count_with_values():
    assert tuple_count(('a', 'a', 'b', 'b', 'b', 'c', 'd')) == {'b': 3, 'd': 1, 'a': 2, 'c': 1}
