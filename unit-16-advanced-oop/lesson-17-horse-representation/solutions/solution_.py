class Horse(object):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return "{name} the {breed}".format(
            name=self.name, breed=self.breed)

    def __repr__(self):
        return "Horse: {name}, {breed}".format(
            name=self.name, breed=self.breed)