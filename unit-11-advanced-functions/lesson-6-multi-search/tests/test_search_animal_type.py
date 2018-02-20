expected = [
    {
        "animal_type": "Penguin",
        "street_name": "Formal Chicken",
        "given_name": "Mclovin"
    },
    {
        "animal_type": "Seagull",
        "street_name": "Beach Chicken",
        "given_name": "Santiago"
    }
]

expected = [{
    'animal_type': 'Penguin',
    'given_name': 'Mclovin',
    'street_name': 'Formal Chicken'
}, {
    'animal_type': 'Seagull',
    'given_name': 'Santiago',
    'street_name': 'Beach Chicken'}
]

def test_search_animal_type():
    #assert False, (search_animals(animals, animal_type="Chicken"))
    assert search_animals(animals, animal_type="Chicken") == expected
