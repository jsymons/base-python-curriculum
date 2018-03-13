def test_salaried():
    emp1 = SalariedEmployee("Bill", 60000)

    assert emp1.name == "Bill"
    assert emp1.salary == 60000

    assert emp1.calculate_annual_income() == 60000
    assert str(emp1) == "Bill makes 60000 annually"
