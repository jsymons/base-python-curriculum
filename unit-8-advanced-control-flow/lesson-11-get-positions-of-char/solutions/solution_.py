def get_positions_of_char(another_string, char_being_searched_for):
    result = ""
    for pos, char in enumerate(another_string):
        if char == char_being_searched_for:
            result += str(pos) + ','
    return result