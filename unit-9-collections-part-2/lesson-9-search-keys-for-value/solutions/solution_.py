def search_keys_for_value(a_dictionary, search_term):
    result_set = set()
    for key, value in a_dictionary.items():
        if value == search_term:
            result_set.add(key)
    return result_set
