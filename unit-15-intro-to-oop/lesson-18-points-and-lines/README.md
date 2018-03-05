# Points and Lines

Time to make things a bit more complicated. Now you need to write _two_ classes!

Create a class `Point` that receives two parameters `x` and `y` and stores them within each point created.

Next create a class `Line` that receives two points as parameters `p1` and `p2`.

It needs the following 3 methods:
* `slope` that returns the slope of the line based on the two points 
    Equation: **(y2 - y1)/(x2 - x1)**
* `y_intercept` that returns the y-intercept of the line
    Equation: **y1 - (slope * x1)**
* `formula` that returns a string of the formula of the line (if the slope is 1, omit it).
    Equation: **y = mx + b** where m is slope and b is y-intercept

Note: None of these methods receive any external parameters

For the `formula` string, if the y-intercept can be truncated (e.g. using 1 instead of 1.0), do it using {:g} in your string formatting. 

```python
"{:g}".format(3.0) # 3
"{:g}".format(3.2) # 3.2
```

Example:

```python
p1 = Point(0, 1)
p2 = Point(1, 2)

l = Line(p1, p2)

l.slope() # 1
l.y_intercept() # 1
l.formula() # 'y = x + 1.0'
```