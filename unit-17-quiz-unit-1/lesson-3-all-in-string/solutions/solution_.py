def all_in_string(a_string, s1, s2, s3):
    total = 0
    if s1 in a_string:
        total += 1

    if s2 in a_string:
        total += 1

    if s3 in a_string:
        total += 1

    return total
