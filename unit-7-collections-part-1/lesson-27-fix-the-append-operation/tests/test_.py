def test_append():
    list_1 = []
    append_elem_to_list(list_1, 'X')

    assert list_1 == ['X']

    list_2 = [3, 2, 1]
    append_elem_to_list(list_2, 9)

    assert list_2 == [3, 2, 1, 9]
