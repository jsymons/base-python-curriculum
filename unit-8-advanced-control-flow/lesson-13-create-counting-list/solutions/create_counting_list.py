def create_counting_list(count_to_number):
    counting_list = []
    count = 0
    if count_to_number >= 0:
        while count < count_to_number:
            count += 1
            counting_list.append(count)
        return counting_list
    return 'cannot be negative'
