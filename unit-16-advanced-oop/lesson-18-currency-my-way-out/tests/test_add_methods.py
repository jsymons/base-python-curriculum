def test_add_methods():
    c1 = Currency(1, 'AUD')
    c2 = Currency(5, 'USD')
    c3 = Currency(100, 'CAD')
    c4 = Currency(2, 'USD')

    assert c1 + c2 == Currency(5.7874, 'USD')
    assert c1 + c3 == Currency(78.9124, 'USD')
    assert c2 + c3 == Currency(83.125, 'USD')
    assert c2 + c4 == Currency(7, 'USD')

    # __radd__
    assert 4 + c2 == Currency(9, 'USD')
    assert 1 + c3 == Currency(79.125, 'USD')

    # __iadd__
    c1 += Currency(3, 'AUD')
    assert c1.value == 4
    assert c1.unit == 'AUD'

    c2 += Currency(100, 'MXN')
    assert c2.value == 10.3706
    assert c2.unit == 'USD'
