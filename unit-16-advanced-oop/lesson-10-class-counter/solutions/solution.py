class Cookie(object):
    COUNT = 0

    def __init__(self):
        Cookie.COUNT += 1

    @classmethod
    def count(cls):
        return cls.COUNT

    @classmethod
    def reset_counter(cls):
        cls.COUNT = 0
