# Cached Calculator

Write a class `Calculator` that has the same methods as the previous one (`add` and `subtract`). But it should also have an attribute `cache` that keeps track of the operations being already performed as a dictionary (see example below and test cases). If the operation was already performed, the method should return the value from the cache. Example:

```python
>>> c = Calculator()
>>> c.cache
{}
>>> c.add(2, 3)
5
>>> c.cache
{
  'add': [
    (2, 3, 5)
  ]
}
>>> c.subtract(8, 2)
6
>>> c.cache
{
  'add': [
    (2, 3, 5)
  ],
  'subtract': [
    (8, 2, 6)
  ]
}
>>> c.add(9, 3)
12
>>> c.cache
{
  'add': [
    (2, 3, 5),
    (9, 3, 12)
  ],
  'subtract': [
    (8, 2, 6)
  ]
}
# Same method invoked again:
>>> c.add(2, 3)  # Should be returned from the cache
5
```
