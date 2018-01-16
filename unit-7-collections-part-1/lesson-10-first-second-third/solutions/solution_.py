def insert_human(a_list, position, elem):
    if position == 'first':
        index = 0
    elif position == 'second':
        index = 1
    elif position == 'third':
        index = 2
    elif position == 'last':
        index = len(a_list)

    a_list.insert(index, elem)
