def test_convert_to_meters():
    d1 = Distance(4, "ft")
    d2 = Distance(1)
    d3 = Distance(1, 'm')
    d4 = Distance(1000, "mm")
    d5 = Distance(1.5, "km")

    assert d1.convert_to_meters() == 1.2192
    assert d2.convert_to_meters() == 1
    assert d3.convert_to_meters() == 1
    assert d4.convert_to_meters() == 1
    assert d5.convert_to_meters() == 1500
