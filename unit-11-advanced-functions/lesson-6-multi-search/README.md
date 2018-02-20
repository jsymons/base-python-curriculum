# Multi-search

Write a function `search_animals` that receives 3 parameters:
* a required parameter called `list_of_animals` that receives a list of animal dictionaries
* an optional parameter called `given_name` that will be used as an optional search term
* an optional parameter called `animal_type` that will be used as an optional search term

First, take a good look at the structure of the example animal list.

```python
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
```

The goal is to be able to search this list of animals by the animal's `given_name` and/or the `animal_type`, for each of those combinations.

Optional arguments enable you to have these types of search combinations. 

If they enter a `given_name` search term, you'll want to check all the animals in the list and see if the search term is in their value associated with the key `given_name`.

There could be multiple matches, so we want to store our matching animal dictionaries in a list.

Do the same thing for `animal_type` search term, but for that check if the search term is in either the value associated with the key `animal_type` OR `street_name`. Hope you remembered your operators lessons :)

Your default values here should be set to `None` by default so it is easy to check what kind of search the user is doing based on which of the optional arguments aren't `None`.

Best of luck!

```python
search_animals(animals, given_name="Will Ferret") == [
        {
            "animal_type": "Ferret",
            "street_name": "Cat Snake",
            "given_name":  "Will Ferret"
        }]
```

