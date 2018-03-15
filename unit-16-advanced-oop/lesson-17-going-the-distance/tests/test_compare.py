def test_str_repr():
    d1 = Distance(4, "ft")
    d2 = Distance(1)
    d3 = Distance(1000, "mm")

    assert d2 == d3
    assert d1 != d2
    assert d1 > d2
    assert d2 < d1
    assert d1 <= d3
    assert d3 >= d1
