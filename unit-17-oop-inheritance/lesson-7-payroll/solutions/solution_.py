class Payroll(object):
    def __init__(self, company, employee_list=None):
        self.company = company
        if not employee_list:
            employee_list = []
        self.employee_list = employee_list

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def get_annual_payroll_cost(self):
        total = 0
        for employee in self.employee_list:
            total += employee.calculate_annual_income()
        return total


class Employee(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{name} makes {income} annually".format(name=self.name, income=self.calculate_annual_income())


class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super(SalariedEmployee, self).__init__(name)
        self.salary = salary

    def calculate_annual_income(self):
        return self.salary


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage):
        super(HourlyEmployee, self).__init__(name)
        self.hourly_wage = hourly_wage

    def calculate_annual_income(self):
        return self.hourly_wage * 40 * 52