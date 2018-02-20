animals = [
        {
            "animal_type": "Raccoon",
            "street_name": "Trash Panda",
            "given_name":  "Gizmo"
        },
        {
            "animal_type": "Snake",
            "street_name": "Danger Noodle",
            "given_name":  "Spaghetti"
        },
        {
            "animal_type": "Snake",
            "street_name": "Danger Noodle",
            "given_name":  "Nope"
        },
        {
            "animal_type": "Penguin",
            "street_name": "Formal Chicken",
            "given_name":  "Mclovin"
        },
        {
            "animal_type": "Sting ray",
            "street_name": "Sea Pancake",
            "given_name":  "Flap Flap"
        },
        {
            "animal_type": "Guinea Pig",
            "street_name": "Furry Potato",
            "given_name":  "Alf"
        },
        {
            "animal_type": "Platypus",
            "street_name": "Duck Puppy",
            "given_name":  "Bill"
        },
        {
            "animal_type": "Seagull",
            "street_name": "Beach Chicken",
            "given_name":  "Santiago"
        },
        {
            "animal_type": "Ferret",
            "street_name": "Cat Snake",
            "given_name":  "Will Ferret"
        }
]

def test_no_search_terms():
    assert search_animals(animals) == []