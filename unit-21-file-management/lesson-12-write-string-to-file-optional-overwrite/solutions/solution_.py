def write_string(filepath, a_string, overwrite_all=False):
    if overwrite_all:
        with open(filepath, "w") as f:
            f.write(a_string + "\n")
    else:
        with open(filepath, "a") as f:
            f.write(a_string + "\n")