class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        return "{name} says {sound}".format(name=self.name, sound=self.sound)


class Cow(Animal):
    def __init__(self, name):
        super(Cow, self).__init__(name)
        self.sound = "moo"


class Sheep(Animal):
    def __init__(self, name):
        super(Sheep, self).__init__(name)
        self.sound = "baaaaa"


class Fox(Animal):
    def __init__(self, name):
        super(Fox, self).__init__(name)
        self.sound = "Ring-ding-ding-ding-dingeringeding"