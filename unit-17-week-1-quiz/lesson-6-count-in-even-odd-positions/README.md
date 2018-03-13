# Count in even-odd positions

We're going to extend our counting from strings by adding a subtle twist. You'll need to write a `count_in_position` function that receives three parameters: a word/sentence, a character to find, and a modifier like `even` or `odd`. Example:

```python
# Example 1
#         0123456789
phrase = 'aXbcXdXXeX'
count_in_position(phrase, 'X', 'even')  # 2
```

Example 1 returns only `2` because there are only `2` characters `X` with an even index/position (positions 4 and 6). Let's see another example; using the same phrase, if we ask for `'odd'` positions we'd get:

```python
# Example 2
#         0123456789
phrase = 'aXbcXdXXeX'
count_in_position(phrase, 'X', 'odd')  # 3
```

We get `3`, because we have three `'X'` with an odd index/position (positions 1, 7 and 9).
