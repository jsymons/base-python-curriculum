def test_compare_equality():
    c1 = Currency(1.27, 'AUD')
    c2 = Currency(1, 'USD')
    c3 = Currency(2, 'CAD')

    assert c1 == c2
    assert c1 != c3
    assert c2 != c3
