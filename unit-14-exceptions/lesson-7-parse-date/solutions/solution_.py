from datetime import datetime


def parse_dates(date_string):
    formats = [
        '%B %d, %Y',
        '%B %d, %y',
        '%A %B %d, %Y',
        '%a %B %d, %Y',
        '%A %d of %B, %Y',
    ]

    for format in formats:
        try:
            return datetime.strptime(date_string, format)
        except ValueError:
            pass

    raise ValueError('Invalid Date Format')