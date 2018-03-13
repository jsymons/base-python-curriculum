def test_payroll():
    emp1 = SalariedEmployee("Bill", 60000)
    emp2 = HourlyEmployee("Ted", 25)
    
    payroll = Payroll("Excellent Adventures")
    assert payroll.company == "Excellent Adventures"

    payroll.add_employee(emp1)
    payroll.add_employee(emp2)
    assert payroll.get_annual_payroll_cost() == 112000
