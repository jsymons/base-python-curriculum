def test_hourly():
    emp1 = HourlyEmployee("Ted", 25)

    assert emp1.name == "Ted"
    assert emp1.hourly_wage == 25

    assert emp1.calculate_annual_income() == 52000
    assert str(emp1) == "Ted makes 52000 annually"
    