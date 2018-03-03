def test_area_valid_values():
    assert round(usa.area(unit='km2')) == 9833520
    assert round(usa.area()) == 9833520
    assert round(usa.area(unit='mi2')) == 3796722
    assert round(usa.area(unit='acres')) == 2428879440
    assert round(usa.area(unit='hectares')) == 983352000

    assert round(canada.area(unit='km2')) == 9984670
    assert round(canada.area()) == 9984670
    assert round(canada.area(unit='mi2')) == 3855081
    assert round(canada.area(unit='acres')) == 2466213490
    assert round(canada.area(unit='hectares')) == 998467000
