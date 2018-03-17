try:
    reduce
except NameError:
    from functools import reduce

def comma_code(a_list):
    return reduce(lambda x, y: x + ", " + y if y != a_list[len(a_list)-1] else x + " and " + y, a_list)
