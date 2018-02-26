import pytest


def test_recipe_too_many_cals():
    ingredients = [
        UNIT_OF_BACON,
        UNIT_OF_BUTTER,
        UNIT_OF_BUTTER,
        UNIT_OF_EGG,
        UNIT_OF_EGG,
        UNIT_OF_EGG
    ]
    with pytest.raises(TooManyCalsException):
        recipe_calculator(ingredients)