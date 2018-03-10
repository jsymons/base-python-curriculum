def test_str_repr():
    c1 = Currency(1.1, 'CAD')
    c2 = Currency(2.5, 'USD')
    c3 = Currency(150, 'MXN')

    assert str(c1) == 'CAD$1.1'
    assert str(c2) == 'USD$2.5'
    assert str(c3) == 'MXN$150'

    assert repr(c1) == "Currency(1.1, 'CAD')"
    assert repr(c2) == "Currency(2.5, 'USD')"
    assert repr(c3) == "Currency(150, 'MXN')"
