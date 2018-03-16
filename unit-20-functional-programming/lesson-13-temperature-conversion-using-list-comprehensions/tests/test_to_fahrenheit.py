def test_to_fahrenheit():
    assert to_fahrenheit([0, 10, 25, 30, 100]) == [32.0, 50.0, 77.0, 86.0, 212.0]
