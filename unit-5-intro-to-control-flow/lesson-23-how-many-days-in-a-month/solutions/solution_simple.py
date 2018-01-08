def how_many_days_in(month):
    if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
        return 31
    elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
        return 30
    else:  # Only February left
        return 28
