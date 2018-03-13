def censor_dictionary(unclean_dictionary, flagged_word):
    removal_list = []
    for word, description in unclean_dictionary.items():
        if flagged_word in description:
            removal_list.append(word)
    for word in removal_list:
        unclean_dictionary.pop(word, None)
    return unclean_dictionary