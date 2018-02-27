def pop(dictionary, key, default_value=None):
    try:
        val = dictionary[key]
        del dictionary[key]
        return val
    except KeyError as e:
        if default_value:
            return default_value
        raise e