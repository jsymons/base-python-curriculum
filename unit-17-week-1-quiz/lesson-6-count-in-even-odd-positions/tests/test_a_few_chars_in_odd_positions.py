def test_a_few_chars_in_odd_positions():
    #         0123456789
    phrase = 'aXbcXdXXeX'
    assert count_in_position(phrase, 'X', 'odd') == 3


def test_only_one_char_in_odd_positions():
    #         0123456789
    phrase = 'aXXbcdXfXg'
    assert count_in_position(phrase, 'X', 'odd') == 1
