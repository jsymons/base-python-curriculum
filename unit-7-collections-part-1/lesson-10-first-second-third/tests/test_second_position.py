def test_second_position():
    list_1 = ['a', 'b', 'c']

    insert_human(list_1, 'second', 'X')
    assert list_1 == ['a', 'X', 'b', 'c']
