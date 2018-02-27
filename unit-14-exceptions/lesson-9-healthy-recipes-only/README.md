# Healthy Recipes Only

Complete the function `recipe_calculator` so that it receives a list of recipe `ingredients` that have calories and a sweetness rating associated with each of them in the dictionaries in your main.py file.

Add up the total sweetness of all the items in the recipe and if they exceed a total sweetness of 8, raise a custom exception TooSweetException.

Then add up the total calories of all the items in the recipe and if they exceed a calorie total of 800, raise a custom exception TooManyCalsException.

If the recipe does not raise an exception, return a tuple of (total_sweetness, total_calories).

```python
ingredients = [
    UNIT_OF_EGG,
    UNIT_OF_FLOUR,
    UNIT_OF_WATER,
    UNIT_OF_EGG,
    UNIT_OF_BUTTER
]

recipe_calculator(ingredients) # (2, 450)

ingredients = [
    UNIT_OF_BACON,
    UNIT_OF_BUTTER,
    UNIT_OF_BUTTER,
    UNIT_OF_EGG,
    UNIT_OF_EGG,
    UNIT_OF_EGG
]

recipe_calculator(ingredients) # Raises TooManyCalsException
```