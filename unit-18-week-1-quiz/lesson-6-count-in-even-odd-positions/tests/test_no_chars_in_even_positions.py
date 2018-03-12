def test_no_chars_in_even_positions():
    #         0123456789
    phrase = 'aXbXcdeXfX'
    assert count_in_position(phrase, 'X', 'even') == 0
