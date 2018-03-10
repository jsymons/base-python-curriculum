def test_convert_target_to_target():
    c1 = Currency(1, 'AUD')
    c2 = Currency(1, 'EUR')

    aud_to_eur = c1.convert('EUR')
    aud_to_mxn = c1.convert('MXN')
    eur_to_jpy = c2.convert('JPY')
    eur_to_arg = c2.convert('ARG')

    assert aud_to_eur.value == 0.6378
    assert aud_to_mxn.value == 14.6614
    assert eur_to_jpy.value == 131.8519
    assert eur_to_arg.value == 24.9877
