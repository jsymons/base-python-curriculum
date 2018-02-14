def sum_of_dict_values(d1, d2, d3):
    result = {}
    for key, value in d1.items():
        result.setdefault(key, 0)
        if result[key] is not None and type(value) is int:
            result[key] += value
        else:
            result[key] = None

    for key, value in d2.items():
        result.setdefault(key, 0)
        if result[key] is not None and type(value) is int:
            result[key] += value
        else:
            result[key] = None

    for key, value in d3.items():
        result.setdefault(key, 0)
        if result[key] is not None and type(value) is int:
            result[key] += value
        else:
            result[key] = None
    return result