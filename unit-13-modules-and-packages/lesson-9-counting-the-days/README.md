# Counting the Days

The datetime library is useful for much more than just getting and formatting dates!

You can let Python perform mathy calculations for you as well.

For this exercise, create a function `counting_the_days` that receives a variable `start_date` and `end_date`. Subtract `start_date` from `end_date` and you will produce a `timedelta` object. To practice using this, return your timedelta object in the format of days using they `days` method.

Example:

```python
counting_the_days(date(1987, 9, 29), date(2017, 9, 29)) # 10958
```