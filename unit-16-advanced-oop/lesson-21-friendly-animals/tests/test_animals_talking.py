def test_animals_talking():
    cat = Cat()
    dog = Dog()
    human = Human()

    assert isinstance(cat, Animal)
    assert isinstance(dog, Animal)
    assert isinstance(human, Animal)

    assert cat.talk() == 'Meow!'
    assert dog.talk() == 'Ruff!'
    assert human.talk() == 'Hello!'