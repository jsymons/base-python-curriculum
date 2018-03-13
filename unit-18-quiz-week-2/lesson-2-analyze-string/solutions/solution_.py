def count_words(a_string):
    words = a_string.split(" ")
    word_count = {}
    for word in words:
        # could also be expressed as:
        # word_count[word] = word_count.get(word, 0) + 1
        word_count.setdefault(word, 0)
        word_count[word] += 1
    return word_count


def get_list_of_duplicates(word_count_dict):
    duplicate_list = []
    for word, count in word_count_dict.items():
        if word not in duplicate_list and count > 1:
            duplicate_list.append(word)
    return sorted(duplicate_list)
