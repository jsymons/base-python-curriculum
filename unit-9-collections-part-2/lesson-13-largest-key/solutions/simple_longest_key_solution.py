def longest_key(a_dict):
    longest = None
    for key in a_dict.keys():
        if not longest or len(key) > len(longest):
            longest = key
    return longest
