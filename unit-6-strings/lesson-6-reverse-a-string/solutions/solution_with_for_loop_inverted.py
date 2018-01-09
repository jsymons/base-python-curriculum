def reverse_string(a_string):
    result = ''
    for idx in range(len(a_string) - 1, -1, -1):
        result += a_string[idx]
    return result
