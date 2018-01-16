def test_with_many_none_value():
    assert check_if_none(None, 2, 'a', 8, None) == True
    assert check_if_none(None, None, None, None, None) == True
