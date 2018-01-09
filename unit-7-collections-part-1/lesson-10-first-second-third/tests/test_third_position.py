def test_third_position():
    list_1 = ['a', 'b', 'c']

    insert_human(list_1, 'third', 'X')
    assert list_1 == ['a', 'b', 'X', 'c']
