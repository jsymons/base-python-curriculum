def char_in_string(a_string, char_to_look_for):
    count = 0
    while count < len(a_string):
        if char_to_look_for == a_string[count]:
            return True
        count += 1
    return False
