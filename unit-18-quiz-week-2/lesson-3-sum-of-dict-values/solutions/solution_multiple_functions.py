def _add_values_to_dict(processing_dict, agg_dict):
    for key, value in processing_dict.items():
        agg_dict.setdefault(key, 0)
        new_value = None
        if type(value) is int and agg_dict[key] is not None:
            new_value = agg_dict[key] + value
        agg_dict[key] = new_value


def sum_of_dict_values(d1, d2, d3):
    result = {}

    _add_values_to_dict(d1, result)
    _add_values_to_dict(d2, result)
    _add_values_to_dict(d3, result)

    return result
