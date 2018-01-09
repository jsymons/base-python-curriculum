def count_elems_with_s(list_of_treasure):
    count = 0
    for treasure in list_of_treasure:
        if 's' in treasure:
            count += 1
    return count