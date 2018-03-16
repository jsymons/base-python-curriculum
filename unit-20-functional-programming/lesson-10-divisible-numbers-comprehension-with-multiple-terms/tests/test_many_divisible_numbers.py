def test_many_divisible_numbers():
    result = divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3])
    expected = [12, 6]

    assert result == expected
