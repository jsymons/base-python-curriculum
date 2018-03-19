def max_lines(*file_names):
    max_name = ""
    max_lines = 0
    for file_name in file_names:
        with open(file_name) as fp:
            read_data = fp.readlines()
            if len(read_data) >= max_lines:
                max_lines = len(read_data)
                max_name = file_name
    return max_name