def tuple_count(a_tuple):
    result_dict = {}
    for item in a_tuple:
        if item not in result_dict.keys():
            result_dict[item] = 0
        result_dict[item] += 1
    return result_dict