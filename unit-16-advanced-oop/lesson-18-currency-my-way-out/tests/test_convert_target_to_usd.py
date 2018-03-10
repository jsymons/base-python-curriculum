def test_convert_target_to_usd():
    c1 = Currency(1, 'AUD')
    c2 = Currency(1, 'MXN')
    c3 = Currency(1, 'EUR')
    c4 = Currency(1, 'JPY')
    c5 = Currency(1, 'USD')

    c1_to_usd = c1.convert('USD')
    c2_to_usd = c2.convert('USD')
    c3_to_usd = c3.convert('USD')
    c4_to_usd = c4.convert('USD')
    c5_to_usd = c5.convert('USD')

    assert c1_to_usd.value == 0.7874
    assert c2_to_usd.value == 0.0537
    assert c3_to_usd.value == 1.2346
    assert c4_to_usd.value == 0.0094
    assert c5_to_usd.value == 1
