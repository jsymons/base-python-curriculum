# Parse Date

Complete the function `parse_dates` built to parse a `date_string` in 5 different acceptable formats (see examples below), parses it, and returns a datetime object of that date.

Use `try/except` clauses to try and parse the dates in each format and if none of them work, raise a ValueError.

Hint: You'll need to use `datetime.strptime` to do this one.

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

Helpful strptime formatting codes:
%B = Full Month Name
%d = 2-digit Day Number for the Month
%Y = 4-digit Year
%y = 2-digit Year
%A = Full Weekday Name
%a = Abbreviated Weekday Name

To do this, you'd do something like the following in your code:
```python
date_string = 'Mon January 03, 2018'
format = '%a %B %d, %Y'

datetime.strptime(date_string, format) # datetime(2018, 1, 3)
```

You'll need to use the formatting codes to figure out all 5 of the possible date formats. Make sure you cover all 5 formats used as parameters in the examples below.


Examples:

```python
parse_dates('Mon January 03, 2018') # datetime(2018, 1, 3)

parse_dates('Monday January 03, 2018') # datetime(2018, 1, 3)

parse_dates('Monday 03 of January, 2018') # datetime(2018, 1, 3)

parse_dates('January 03, 18') # datetime(2018, 1, 3)

parse_dates('January 03, 2018') # datetime(2018, 1, 3)

parse_dates('INVALID DATE') # Raises ValueError
```