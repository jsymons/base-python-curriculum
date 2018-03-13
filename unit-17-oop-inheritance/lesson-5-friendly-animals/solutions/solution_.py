class Animal(object):
    pass


class Cat(Animal):
    def talk(self):
        return "Meow!"


class Dog(Animal):
    def talk(self):
        return "Ruff!"


class Human(Animal):
    def talk(self):
        return "Hello!"