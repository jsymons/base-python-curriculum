def censor_dictionary(unclean_dictionary, flagged_word):
    for word, description in unclean_dictionary.items():
        if flagged_word in description:
            unclean_dictionary.pop(word, None)
    return unclean_dictionary