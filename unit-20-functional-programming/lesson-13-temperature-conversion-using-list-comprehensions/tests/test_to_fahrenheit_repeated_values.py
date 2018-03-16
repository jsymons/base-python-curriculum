def test_to_fahrenheit_repeated_values():
    assert to_fahrenheit([0, 10, 10, 100]) == [32.0, 50.0, 50.0, 212.0]
