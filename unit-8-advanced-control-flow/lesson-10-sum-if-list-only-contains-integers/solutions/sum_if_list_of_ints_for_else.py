def sum_if_list_of_ints(a_list):
    for item in a_list:
        if not isinstance(item, int):
            break
    else:
        return sum(a_list)
    return 'not an int'
