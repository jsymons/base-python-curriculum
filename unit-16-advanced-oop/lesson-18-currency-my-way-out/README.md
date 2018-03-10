# Currency My Way Out

Complete the methods for the class `Currency` so that it has functionality to compare and perform basic math operations on Currencies.

You can see in the editor that we have a dictionary containing the exchange rates of many currencies (`MXN`, `EUR`, `ARG`, etc). But they're all expressed in US Dollars (`USD`). So, how do you convert from (for example) `EUR` > `MXN`? Well, you have to go through `USD` first. The `convert` method takes any pair of currencies (as in our previous example `EUR` > `MXN`) and converts them (`EUR` to `MXN`). As we mentioned, you have to convert it to `USD` first, so the pseudocode looks something like:

```
# Objective: EUR > MXN
# Step 1: Convert EUR > USD (store value in EUR_usd)
# Step 2: Convert EUR_usd to > MXN
```
Probably makes more sense in this example:

```python
# 4 EUR to MXN
# 4 / 0.81 (EUR conversion to USD) * 18.62 (MXN conversion from USD) == 91.95
```

This has similar magic methods to the Distance assignment, but now there additional ones to teach your class how to be added and (optionally) subtracted.

Use [this guide](https://rszalski.github.io/magicmethods/) for magic method guidance, and read the tests if you get stuck.

**IMPORTANT:** To avoid rounding issues, round your conversion up to 4 decimals (`round(value, 4)`). For example, to convert from `AUD` > `USD` you have to do (`1 / 1.27`) which yields a result with too many decimals: `0.7874015748031495`. Round it to 4 decimals to get the expected result: `round(0.7874015748031495, 4) == 0.7874`.
