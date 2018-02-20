expected_animal_types = [{
    'animal_type': 'Penguin',
    'given_name': 'Mclovin',
    'street_name': 'Formal Chicken'
}, {
    'animal_type': 'Seagull',
    'given_name': 'Santiago',
    'street_name': 'Beach Chicken'}
]

def test_search_animal_type():
    assert search_animals(animals, animal_type="Chicken") == expected_animal_types
