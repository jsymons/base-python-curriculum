# Guess the pattern

This is the first "Guess the Pattern" lesson. Use the tests below to find the pattern of the function `my_function`. This is a "reverse engineer process", where you don't have any guidelines, you just know what the function receives, and what the function returns.

Your job is to figure out the pattern and implement it in `my_function`.

**Only for this first lesson**, we'll provide more details; for the following ones you'll use only the tests.

Let's read the first test:

```python
assert my_function(2) == 4
```

The way to "reverse" these functions is by understanding the _Input_ and _Output_ of the function, its [_interface_](https://en.wikipedia.org/wiki/Interface_%28computing%29).

* The input of the function is a number: `2`
* The output is another number: `4`

We don't know the internals of the function, that's what we need to figure out. But we can clearly see that, at least in this first example, what the function is doing is _doubling_ the input number (`2` > `4`).

You can take it from here...
