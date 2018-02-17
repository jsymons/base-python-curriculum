def test_invalid_box_height():
    assert create_empty_box(1, 4, 'Y') == "Invalid box dimensions"
