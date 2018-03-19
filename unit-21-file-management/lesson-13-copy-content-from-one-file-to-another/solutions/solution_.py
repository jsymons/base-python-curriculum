def copy_file(source_file, target_file):
    with open(source_file, "r") as s:
        read_data = s.read()
    with open(target_file, "w") as t:
        t.write(read_data) 