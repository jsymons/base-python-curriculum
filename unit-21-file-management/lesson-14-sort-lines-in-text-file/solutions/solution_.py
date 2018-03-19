def sort_lines(filepath, sorting='asc'):
    with open(filepath, "r") as f:
        read_data = f.readlines()
    if sorting == 'asc':
        read_data.sort()
    else:
        read_data.sort(reverse=True)
    with open(filepath, "w") as f:
        for line in read_data:
            f.write(line)