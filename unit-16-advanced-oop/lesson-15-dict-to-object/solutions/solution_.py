class Commercial(object):
    def __init__(self, a_dictionary):
        for key, value in a_dictionary.items():
            setattr(self, key, value)
