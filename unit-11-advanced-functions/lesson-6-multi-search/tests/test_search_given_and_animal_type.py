expected = [{
    "animal_type": "Snake",
    "street_name": "Danger Noodle",
    "given_name": "Nope"
}]

def test_search_given_and_animal_type():
    assert search_animals(animals, animal_type="Snake", given_name="Nope") == expected
