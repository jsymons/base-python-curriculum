def insert_dashes(a_string):
    counter = 1
    res = ""
    while counter <= len(a_string):
        char = a_string[counter - 1]
        res += char
        if counter % 3 == 0:
            res += '-'
        counter += 1
    return res
