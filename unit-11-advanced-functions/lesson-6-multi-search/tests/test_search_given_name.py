expected = [{
    "animal_type": "Ferret",
    "street_name": "Cat Snake",
    "given_name": "Will Ferret"
}]

def test_search_given_name():
    assert search_animals(animals, given_name="Will Ferret") == expected
