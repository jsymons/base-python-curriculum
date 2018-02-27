import pytest


def test_recipe_is_too_sweet():
    ingredients = [
        UNIT_OF_CHOCOLATE,
        UNIT_OF_SUGAR,
        UNIT_OF_SUGAR,
        UNIT_OF_SUGAR,
        UNIT_OF_BUTTER
    ]
    with pytest.raises(TooSweetException):
        recipe_calculator(ingredients)