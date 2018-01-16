def count_in_position(a_string, a_char, position_type):
    count = 0
    for index, current_char in enumerate(a_string):
        if a_char == current_char:
            if position_type == 'even' and index % 2 == 0:
                count += 1
            elif position_type == 'odd' and index % 2 != 0:
                count += 1

    return count
