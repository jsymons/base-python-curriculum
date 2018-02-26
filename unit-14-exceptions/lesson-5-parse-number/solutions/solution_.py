def parse_number(number):
    try:
        return int(number)
    except ValueError:
        pass

    try:
        return float(number)
    except ValueError:
        pass

    raise ValueError("Invalid number")