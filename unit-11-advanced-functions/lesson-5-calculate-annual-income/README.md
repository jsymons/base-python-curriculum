# Calculate Annual Income

Write a function `calculate_annual_income` with two parameters: `hourly_rate` and `hours_per_week`. You could design `hours_per_week` to be a required parameter, but for this assignment, since many people work 40 hours per week, you're going to design it as a default/optional argument set to 40.

There are 52 weeks in a year, so all we need to do is multiply the `hourly_rate` by `hours_per_week` and multiply that by 52. 

```python
calculate_annual_income(15.00)  # 31200.00
calculate_annual_income(12.00, hours_per_week=20) # 12480.00
```