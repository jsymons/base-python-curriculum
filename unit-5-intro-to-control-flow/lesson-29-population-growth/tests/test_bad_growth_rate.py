def test_bad_growth_rate():
    assert population_growth(5000, 0, 40000) == 'invalid growth rate'
