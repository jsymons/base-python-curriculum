def sum_if_list_of_ints(a_list):
    for item in a_list:
        if not isinstance(item, int):
            return 'not an int'
    return sum(a_list)
