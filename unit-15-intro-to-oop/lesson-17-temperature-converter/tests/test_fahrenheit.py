def test_fahrenheit():
    t = TempConverter(fahrenheit=90)
    assert t.to_celsius() == 32.2
    assert t.to_fahrenheit() == 90