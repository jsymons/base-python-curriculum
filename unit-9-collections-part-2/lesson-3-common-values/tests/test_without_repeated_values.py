def test_without_repeated_values():
    assert common_values((4, 5, 6, 7), (1, 2, 3)) == {1, 2, 3, 4, 5, 6, 7}
