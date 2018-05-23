def find_max_char(a_string):
    max_found = ''
    for char in a_string:
        if char > max_found:
            max_found = char
    return max_found
