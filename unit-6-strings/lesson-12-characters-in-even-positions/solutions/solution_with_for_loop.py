def chars_in_even_positions(a_string):
    result = ""
    position = 1
    for char in a_string:
        if position % 2 == 0:
            result += char
        position += 1

    return result
