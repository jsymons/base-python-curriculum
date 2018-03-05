def test_celsius():
    t = TempConverter(celsius=20)
    assert t.to_celsius() == 20
    assert t.to_fahrenheit() == 68