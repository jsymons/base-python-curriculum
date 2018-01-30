def string_of_numbers(length):
    number_string = ""
    count = 1
    while count <= length:
        number_string += str(count)
        count += 1
    return number_string