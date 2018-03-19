# Find Line with String

Write a function that receives a file path and a string as parameters, and
returns the line number where that string is in the file. If the string
is not in the file, it should return None.

Example:
```python
which_line('file1.txt', 'hello world')  # 10
which_line('file1.txt', 'this is not in the file')  # None
```