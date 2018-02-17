def test_invalid_box_width():
    assert create_empty_box(3, 1, '$') == "Invalid box dimensions"
