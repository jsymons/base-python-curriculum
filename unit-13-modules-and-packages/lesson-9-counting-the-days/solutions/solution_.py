# Import the library here!
from datetime import date

def counting_the_days(start_date, end_date):
    return (end_date - start_date).days


print(counting_the_days(date(1987, 9, 29), date(2017, 9, 29)))