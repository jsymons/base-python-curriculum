# Class counter

Create a class `Cookie` that keeps track of how many instances were created. The `Cookie` class should have a `count` method that returns how many `Cookie` objects where instantiated. It should also include other method `reset_counter` that puts the count back to 0. Example:

```python
Cookie.count()  # 0

c1 = Cookie()
c2 = Cookie()
c3 = Cookie()
Cookie.count()  # 3

c4 = Cookie()
c5 = Cookie()

Cookie.count()  # 5

# == COUNTER RESET ==
Cookie.reset_counter()

Cookie.count()  # 0

c6 = Cookie()
c7 = Cookie()
Cookie.count()  # 2
```
