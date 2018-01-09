def get_string_positions(the_string):
    result = ""
    for pos, char in enumerate(the_string):
        result += str(pos) + '-' + char + '\n'
    return result