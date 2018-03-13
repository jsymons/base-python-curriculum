def test_no_chars_in_odd_positions():
    #         0123456789
    phrase = 'abXcXdefXg'
    assert count_in_position(phrase, 'X', 'odd') == 0
