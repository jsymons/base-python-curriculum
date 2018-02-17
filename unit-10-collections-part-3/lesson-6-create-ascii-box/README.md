# Create ASCII Box

Write a function `create_box` that takes three inputs: `height` (rows), `width` (columns), and a character `char` and creates a `height` × `width` box using the character `char`.

For this exercise, it's recommended to use a nested for-loop. There are other ways of solving it (which might be a good starting point), but try reaching the nested for-loop solution.

```python
>>> create_box(3, 4, '*')
'****
 ****
 ****'
>>> create_box(2, 2, '@')
'@@
 @@'
```

**IMPORTANT**: You need to `return` your box, not just print it.
