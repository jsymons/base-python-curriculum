def test_with_repeated_values():
    assert common_values((1, 5, 7, 1, 24), (1, 2, 3, 4)) == {1, 2, 3, 4, 5, 7, 24}
