# Create Empty Box

Expand on the last assigment and write a function `create_empty_box` that takes three inputs: `height` (rows), `width` (columns), and a character `char` and creates a `height` × `width` box using the character `char` that only has characters on the borders of the box (it's not filled in).

If the box `height` or `width` are less than 3, return 'Invalid box dimensions' because it won't be an empty box.

Hint: Look for patterns in the the way the empty box looks when you design your solution (top to bottom, side to side).


```python
>>> create_empty_box(3, 4, '*')
'****
 *  *
 ****'
>>> create_empty_box(5, 5, '@')
'@@@@@
 @   @
 @   @
 @   @
 @@@@@'
>>> create_empty_box(1, 1, '$')
'Invalid box dimensions'
```
