def test_convert_usd_to_target():
    c1 = Currency(1, 'USD')

    in_aud = c1.convert('AUD')
    in_mxn = c1.convert('MXN')
    in_eur = c1.convert('EUR')
    in_usd = c1.convert('USD')

    assert in_aud.value == 1.27
    assert in_mxn.value == 18.62
    assert in_eur.value == 0.81
    assert in_usd.value == 1  # Same
