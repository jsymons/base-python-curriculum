# Price, cost and value

This is a simple assignment to demonstrate the power of Duck Typing. There are three classes already implemented (`Loan`, `Movie`, `Milk`) but each one of them has a different attribute to represent _"value"_. `Loan` has `value`, `Movie` has `price` and `Milk` has `cost`.

Your job is to implement the highly dynamic `calculate` function that takes two objects, that can be of any type (`Loan`, `Movie`, `Milk`) and returns the total of the sum of their attributes. The key is to never check for types and to have a dynamic function with as few hardcoded names as possible.

Once you're done, check the solution and compare!
