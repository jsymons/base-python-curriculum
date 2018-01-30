# Nice Looking Date

Dates and time in Python are stored in a separate data type, the datetime object. The formatting can be a little tricky at first, so it is best to practice with it a fair amount to become familiar. Generally, you'll have the documentation handy for reference.

[Datetime Documentation](https://docs.python.org/3/library/datetime.html)

For the first exercise, you'll want to import the `date` object from `datetime` library by typing `from datetime import date
`. Then create a function called `format_date` that will receive a datetime object `a_date` and return a formatted string of the date. To do that, use the `strftime` method that you'll find in the documentation. Return a string of the formatted as below:

`Weekday, Month Day Year`

Example:

```python
format_date(date(1987, 9, 29)) # "Tuesday, September 29 1987"
```

[strftime info](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)


