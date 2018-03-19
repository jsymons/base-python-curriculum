def which_line(filepath, a_string):
    with open(filepath) as fp:
        read_data = fp.readlines()
        for line_num, line in enumerate(read_data):
            if a_string in line:
                return line_num + 1
        return None