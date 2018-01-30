# Import the library here!
from datetime import date

def celebrate_if_friday(a_date):
    if a_date.strftime("%A") == "Friday":
        return "YES!"
    return "Aww"