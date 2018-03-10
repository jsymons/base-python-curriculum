def test_init():
    d1 = Distance(4, "ft")

    assert d1.value == 4
    assert d1.unit == "ft"