class Location(object):
    def __init__(self, hiding_places):
        for key, value in hiding_places.items():
            setattr(self, key, value)

    def search(self, list_of_guesses):
        prizes = []
        for guess in list_of_guesses:
            if hasattr(self, guess):
                prizes.append(getattr(self, guess))
        return prizes