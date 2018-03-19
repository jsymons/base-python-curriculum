def count_lines(filepath):
    with open(filepath) as fp:
        return len(fp.readlines())