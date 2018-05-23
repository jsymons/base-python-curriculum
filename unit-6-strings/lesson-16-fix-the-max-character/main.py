def find_max_char(a_string):
    # THIS IS BROKEN
    # YOUR JOB IS TO FIX IT
    # You can change this function as much as you want
    max_found = None
    for char in a_string:
        if char > max_found:
            max_found = char
            return max_found
