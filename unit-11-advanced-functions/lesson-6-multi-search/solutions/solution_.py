def search_animals(list_of_animals, given_name=None, animal_type=None):
    if given_name and animal_type:
        for animal in animals:
            if given_name in animal['given_name'] and (animal_type in animal['animal_type'] or animal_type in animal['street_name']):
                result_animals.append(animal)
    elif given_name:
        for animal in animals:
            if given_name in animal['given_name']:
                result_animals.append(animal)
    elif animal_type:
        for animal in animals:
            if animal_type in animal['animal_type'] or animal_type in animal['street_name']:
                result_animals.append(animal)
    return sorted(result_animals)


animals = [
    {
        "animal_type": "Raccoon",
        "street_name": "Trash Panda",
        "given_name": "Gizmo"
    },
    {
        "animal_type": "Snake",
        "street_name": "Danger Noodle",
        "given_name": "Spaghetti"
    },
    {
        "animal_type": "Snake",
        "street_name": "Danger Noodle",
        "given_name": "Nope"
    },
    {
        "animal_type": "Penguin",
        "street_name": "Formal Chicken",
        "given_name": "Mclovin"
    },
    {
        "animal_type": "Sting ray",
        "street_name": "Sea Pancake",
        "given_name": "Flap Flap"
    },
    {
        "animal_type": "Guinea Pig",
        "street_name": "Furry Potato",
        "given_name": "Alf"
    },
    {
        "animal_type": "Platypus",
        "street_name": "Duck Puppy",
        "given_name": "Bill"
    },
    {
        "animal_type": "Seagull",
        "street_name": "Beach Chicken",
        "given_name": "Santiago"
    },
    {
        "animal_type": "Ferret",
        "street_name": "Cat Snake",
        "given_name": "Will Ferret"
    }
]
