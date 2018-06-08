# Positions

Write a function `positions` that receives a string and 3 words, and returns the positions of each in the original string. Example:

```python
# Positions:
#         0                         26      34
phrase = "Python is good. Python is Wise. I like Python"
positions(phrase, 'Python', 'Wise', 'like')  # "0,26,34"
```

If the word doesn't exist in the original string, it should backfill using dashes. Example:

```python
# Positions:
#         0                         26
phrase = "Python is good. Python is Wise. I like Python"
positions(phrase, 'Python', 'Wise', 'Ruby')  # "0,26,-" (Ruby doesn't exist)
```
