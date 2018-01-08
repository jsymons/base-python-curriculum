def which_type(val):
    if isinstance(val, str):
        return 'string'
    elif isinstance(val, bool):
        return 'boolean'
    elif isinstance(val, int):
        return 'integer'
    elif isinstance(val, float):
        return 'float'
