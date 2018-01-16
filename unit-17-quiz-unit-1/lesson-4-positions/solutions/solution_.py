def positions(a_string, first_word, second_word, third_word):
    result = ''
    if first_word in a_string:
        result += str(a_string.index(first_word))
    else:
        result += '-'
    result += ','

    if second_word in a_string:
        result += str(a_string.index(second_word))
    else:
        result += '-'
    result += ','

    if third_word in a_string:
        result += str(a_string.index(third_word))
    else:
        result += '-'

    return result
