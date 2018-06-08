# Population growth

> There's a walkthrough explanation of the solution in this video: [https://youtu.be/xtWsbLAp0IU](https://youtu.be/xtWsbLAp0IU). Notebook can be found [here](https://github.com/rmotr-curriculum/base-python-curriculum/blob/master/unit-5-intro-to-control-flow/lesson-31-population-growth/Population%20Growth%20Explanation.ipynb).

Define a function `population_growth` that receives an initial population,
annual rate of growth, and target population. Use a while loop to calculate 
how many years it takes to go over the target population and return it. If
the annual growth rate is not greater than zero, return 'invalid growth rate'.
Do not use `math.pow` or the `x**y` operator.

Target = `Initial * (1 + rate)^(number of years)`


Examples:

```python
>>> population_growth(5000, 0.1, 10000)
8
>>> population_growth(5000, 0.1, 20000)
15
>>> population_growth(5000, 0.1, 40000)
22
>>> population_growth(5000, 0, 40000)
'invalid growth rate'
```
