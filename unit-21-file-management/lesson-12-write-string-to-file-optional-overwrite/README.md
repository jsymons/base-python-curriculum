# Write String to File Optional Overwrite

Write a function that receives a path to a text file as first parameter,
a string and an optional "ovewrite_all" boolean.
If overwrite_all is false, the function should
append the string at the end of current content in the text file.
If it's true, it should clean the content in the file and
write only given string.

There should always be a new line char at the end of the written line.
See test cases for more details.

Example:
```python
write_string('test-file.txt', 'this is the string', overwrite_all=False)
```