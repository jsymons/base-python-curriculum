def tuple_count(a_tuple):
    result_dict = {}
    for item in a_tuple:
        result_dict.setdefault(item, 0)
        result_dict[item] += 1
    return result_dict