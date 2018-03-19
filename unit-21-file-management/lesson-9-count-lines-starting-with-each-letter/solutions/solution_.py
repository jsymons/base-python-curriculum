import string

def counter_by_letter(filepath):
    result = dict([(letter, 0) for letter in string.ascii_lowercase])
    with open(filepath) as fp:
        read_data = fp.readlines()
        for line in read_data:
            result[line[0]] += 1
        return letters