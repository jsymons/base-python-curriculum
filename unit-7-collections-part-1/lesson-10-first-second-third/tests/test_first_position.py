def test_first_position():
    list_1 = ['a', 'b', 'c']

    insert_human(list_1, 'first', 'X')
    assert list_1 == ['X', 'a', 'b', 'c']
