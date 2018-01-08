def test_without_many_none_value():
    assert check_if_none(0, 2, 'a', 8, 'Z') == False
