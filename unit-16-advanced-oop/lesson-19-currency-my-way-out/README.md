# Currency My Way Out

Complete the methods for the class `Currency` so that it has functionality to compare and perform basic math operations on Currencies.

For the `convert` method, the formula is:
 value / current_currency_unit_conversion_to_USD(from dictionary) * new_currency_unit_conversion_from_USD(also from dicitonary)

Probably makes more sense in this example:

```python
# 4 EUR to MXN
# 4 / 0.81 (EUR conversion to USD) * 18.62 (MXN conversion from USD) == 91.95
```

This has similar magic methods to the Distance assignment, but now there additional ones to teach your class how to be added and subtracted.

Use https://rszalski.github.io/magicmethods/ for magic method guidance, and read the tests if you get stuck.

```python

```