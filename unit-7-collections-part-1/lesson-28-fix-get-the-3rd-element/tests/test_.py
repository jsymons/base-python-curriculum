def test_get_3rd_element():
    list_1 = ['A', 'B', 'C', 'D', 'E']
    assert get_the_3rd_element(list_1) == 'C'

    list_2 = [1, 2, 3, 4, 5]
    assert get_the_3rd_element(list_2) == 3

    list_3 = [9, 9, 9]
    assert get_the_3rd_element(list_3) == 9
