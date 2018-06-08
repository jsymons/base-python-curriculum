# Positions

Write a function `positions` that receives a string and 3 words, and returns the first position of each one of them in the original string. Example:

```python
# Positions:
#         0                         26      34
phrase = "Python is good. Python is Wise. I like Python"
positions(phrase, 'Python', 'Wise', 'like')  # "0,26,34"
```
_(Note that the position of `"Python"` in this case is `0`, because is the first one found)_

If the word doesn't exist in the original string, it should backfill using dashes. Example:

```python
# Positions:
#         0                         26
phrase = "Python is good. Python is Wise. I like Python"
positions(phrase, 'Python', 'Wise', 'Ruby')  # "0,26,-" (Ruby doesn't exist)
```
