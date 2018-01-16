# Palindromic Primes

**Solve this assignment using while loops**

A [palindromic number](https://en.wikipedia.org/wiki/Palindromic_number) is a number that reads the same forwards and backwards. Example: "121" (You read: "one, two, one", forwards and backwards). "1001" ("one, zero, zero, one"), etc.

Write a function `next_palindromic_prime` that receives a number and returns the closest larger number that's both a prime and palindromic.

As we haven't worked with strings in depth yet, we've already provided a function to reverse a string (useful for your `is_palindromic` function).

Examples:

```python
next_palindromic_prime(100) == 101
next_palindromic_prime(150) == 151
next_palindromic_prime(160) == 181
next_palindromic_prime(200) == 313
next_palindromic_prime(10000) == 10301
next_palindromic_prime(12000) == 12421
```

You can use the following list of Palindromic Primes as a reference: [https://oeis.org/A002385](https://oeis.org/A002385).

Wikipedia also has an entry on [Palindromic Primes](https://en.wikipedia.org/wiki/Palindromic_prime).
