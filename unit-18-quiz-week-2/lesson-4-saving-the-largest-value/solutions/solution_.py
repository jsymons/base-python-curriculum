def get_largest_numbers(d1, d2, d3):
    result = {
        "d1": None,
        "d2": None,
        "d3": None
    }

    for key, value in d1.items():
        if type(value) is int and (result["d1"] is None or result["d1"] < value):
            result["d1"] = value

    for key, value in d2.items():
        if type(value) is int and (result["d2"] is None or result["d2"] < value):
            result["d2"] = value

    for key, value in d3.items():
        if type(value) is int and (result["d3"] is None or result["d3"] < value):
            result["d3"] = value
    return result