def subtract_reversed(a_list):
    if len(a_list) == 0:
        return 0

    result = a_list[-1]
    index = 2
    while index <= len(a_list):
        elem = a_list[-1 * index]
        result -= elem
        index += 1

    return result
