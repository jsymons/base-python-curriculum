# String Positions

Sometimes you need to know the position of a character in a string and you might not want to count to figure it out. So write a quick function to do it for you!

Complete `get_string_positions` so that it takes `the_string` and creates a new string showing the position of each character. Example:

```python
print(get_string_positions("xyz"))

'''
Prints:
0-x
1-y
2-z
'''
```

The function uses the `enumerate()` function on the list in a for loop to get each position and character associated with it. Example:

```python
for position, character in enumerate(list_name):
    # do stuff
```

Then just store the result in a big string. Note you separate the lines by using '\n' the newline character after each line. Good luck!

Hint: You might have to put str() around to position to change it from an integer into a string so you can add it to your result string.