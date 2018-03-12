# Payroll

Create a class `Employee` with two subclasses: `SalariedEmployee` and `HourlyEmployee`. 

`Employee` receives a `name` parameter and has a `__str__` method (prints like "[name] makes [annual_income] annually").

`SalariedEmployee` should receive parameters for `name` and `salary`. It has a method `calculate_annual_income` that returns the `salary` for that person.

`HourlyEmployee` should receive parameters for `name` and `hourly_wage`. It has a method `calculate_annual_income` that returns the annual income, calculated by multiplying the `hourly_wage` * 40 (hrs per week) * 52 (weeks).

The `Payroll` class receives a parameter for `company` and an optional argument for `employee_list`. If there is no `employee_list`, set it to an empty list. It has two methods:
- `add_employee` receives an employee as a parameter and adds it to the `employee_list`
- `get_annual_payroll_cost` adds up the total annual income for each employee in the `employee_list` and returns it


Example:

```python
emp1 = SalariedEmployee("Bill", 60000)
emp2 = HourlyEmployee("Ted", 25)

emp1.name # "Bill"
emp1.calculate_annual_income() # 60000
print(emp1) # "Bill makes 60000 annually"

emp1.calculate_annual_income() # 60000
emp2.calculate_annual_income() # 52000

payroll = Payroll("Excellent Adventures")
payroll.company # "Excellent Adventures"

payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.get_annual_payroll_cost() # 112000
```