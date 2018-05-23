def test_find_max_character():
    assert find_max_char('arjbo') == 'r'

    assert find_max_char('ABCDEFGH') == 'H'

    assert find_max_char('HGFEDCBA') == 'H'

    assert find_max_char('a') == 'a'
