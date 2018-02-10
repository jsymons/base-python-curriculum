def get_search_match_indexes(list_being_frisked, search_term):
    list_of_matching_indexes = []
    index = 0
    for item in list_being_frisked:
        if item == search_term:
            list_of_matching_indexes.append(index)
        index += 1
    return list_of_matching_indexes