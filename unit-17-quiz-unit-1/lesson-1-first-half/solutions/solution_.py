def first_half(a_string):
    string_length = len(a_string)
    half_length = int(string_length / 2)
    if string_length % 2 == 0:
        return a_string[:half_length]
    else:
        return a_string[:half_length + 1]
