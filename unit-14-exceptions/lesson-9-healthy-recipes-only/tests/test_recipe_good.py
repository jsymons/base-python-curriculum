def test_recipe_good():
    ingredients = [
        UNIT_OF_EGG,
        UNIT_OF_FLOUR,
        UNIT_OF_WATER,
        UNIT_OF_EGG,
        UNIT_OF_BUTTER
    ]
    assert recipe_calculator(ingredients) == (2, 450)