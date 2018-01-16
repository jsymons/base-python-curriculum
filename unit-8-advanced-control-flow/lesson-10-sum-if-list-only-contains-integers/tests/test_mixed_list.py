def test_mixed_list():
    assert sum_if_list_of_ints([1, 'a', 3]) == 'not an int'
