def write_lines(filepath, list_of_strings):
    with open(filepath, 'w') as fp:
        for line in list_of_strings:
            fp.write(line + "\n")