def test_last_position():
    list_1 = ['a', 'b', 'c']

    insert_human(list_1, 'last', 'X')
    assert list_1 == ['a', 'b', 'c', 'X']
