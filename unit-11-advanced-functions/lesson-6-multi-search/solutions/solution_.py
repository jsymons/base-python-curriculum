def search_animals(list_of_animals, given_name=None, animal_type=None):
    result_animals = []
    for animal in animals:
        if given_name and given_name not in animal['given_name']:
            continue
        if animal_type and animal_type not in animal['animal_type'] and animal_type not in animal['street_name']:
            continue
        result_animals.append(animal)

    return result_animals

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