def neutralize_uppercase(stringy):
    count = 0
    while count < len(stringy):
        if stringy[count] == stringy[count].upper():
            stringy = ""
            break
        count += 1
    return stringy