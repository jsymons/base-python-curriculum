def test_string_to_list():
    assert string_to_list('abc') == ['a', 'b', 'c']
    assert string_to_list('a1b2') == ['a', '1', 'b', '2']
