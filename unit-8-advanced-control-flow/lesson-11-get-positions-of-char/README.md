# Get Positions of Char

Use a for loop with `enumerate` to complete the function `get_positions_of_char` so that it looks at `another_string` and searches for characters that match `char_being_searched_for`. If it's a match, add the position to a result string followed by a comma. Example:

```python
get_positions_of_char("aabcda", "a") # Returns "0,1,5,"
```

Hint: You might have to put str() around to position to change it from an integer into a string so you can add it to your result string.