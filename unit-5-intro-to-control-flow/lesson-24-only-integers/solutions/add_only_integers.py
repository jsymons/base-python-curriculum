def add_only_integers(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return 'invalid parameters'
