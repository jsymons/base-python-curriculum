def test_general_comparison():
    c1 = Currency(1.27, 'AUD')
    c2 = Currency(1, 'USD')
    c3 = Currency(100, 'CAD')

    assert c3 > c1
    assert c1 < c3

    # Same for c2
    assert c3 > c2
    assert c2 < c3

    assert c2 >= c1
    assert c2 <= c1
    assert c1 >= c2
    assert c1 <= c2

    assert c3 >= c1
    assert c1 <= c3
    assert c3 >= c2
    assert c2 <= c3
