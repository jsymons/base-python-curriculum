def read_line_number(filepath, line_number):
    with open(filepath) as fp:
        return fp.readlines()[line_number - 1]