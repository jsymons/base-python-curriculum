def count_occurrences(a_list):
    result_dict = {}
    for elem in a_list:
        if elem not in result_dict.keys():
            result_dict[elem] = 1
        else:
            result_dict[elem] += 1
    return result_dict
