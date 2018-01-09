def test_get_positions():
    assert get_positions_of_char("XabcXdefXjahX", "X") == "0,4,8,12,"
