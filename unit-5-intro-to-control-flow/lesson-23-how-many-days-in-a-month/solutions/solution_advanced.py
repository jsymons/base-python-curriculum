def how_many_days_in(month):
    months_with_31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
    months_with_30 = ['April', 'June', 'September', 'November']
    months_with_28 = ['February']

    if month in months_with_31:
        return 31
    elif month in months_with_30:
        return 30
    elif month in months_with_28:
        return 28
