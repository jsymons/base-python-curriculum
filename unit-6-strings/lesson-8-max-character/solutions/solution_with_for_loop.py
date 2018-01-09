def max_char(a_string):
    max_found = None
    for char in a_string:
        if max_found is None or char > max_found:
            max_found = char

    return max_found or ''
