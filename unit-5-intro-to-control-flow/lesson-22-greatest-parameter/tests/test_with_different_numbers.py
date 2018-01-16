def test_with_different_numbers():
    assert greatest_parameter(2, 4, 9, 1, 1) == 9
    assert greatest_parameter(42, 4, 9, 1, 1) == 42
    assert greatest_parameter(5, 4, 9, 1, 17) == 17
