def test_gdp_per_capita():
    assert round(usa.gdp_per_capita()) == 62014
    assert round(canada.gdp_per_capita()) == 52231
