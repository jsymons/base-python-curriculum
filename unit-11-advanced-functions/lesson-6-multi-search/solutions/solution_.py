def search_animals(list_of_animals, given_name=None, animal_type=None):
    result_animals = []
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