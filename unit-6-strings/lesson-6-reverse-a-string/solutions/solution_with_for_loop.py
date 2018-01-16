def reverse_string(a_string):
    result = ''
    for idx in range(0, len(a_string)):
        result += a_string[len(a_string) - 1 - idx]
    return result
