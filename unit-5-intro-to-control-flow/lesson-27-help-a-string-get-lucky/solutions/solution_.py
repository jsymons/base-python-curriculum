def get_lucky(poor_string, lucky_number):
    count = 0
    while count < lucky_number:
        poor_string += "7"
        count += 1
    return poor_string