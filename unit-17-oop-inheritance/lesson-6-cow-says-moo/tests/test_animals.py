def test_animals():
    cow = Cow('Bessie')
    sheep = Sheep('Fuzzy')
    fox = Fox('Red')

    assert isinstance(cow, Animal)
    assert isinstance(sheep, Animal)
    assert isinstance(fox, Animal)

    assert cow.sound == "moo"
    assert sheep.sound == "baaaaa"
    assert fox.sound == "Ring-ding-ding-ding-dingeringeding"

    assert cow.talk() == "Bessie says moo"
    assert sheep.talk() == "Fuzzy says baaaaa"
    assert fox.talk() == "Red says Ring-ding-ding-ding-dingeringeding"
