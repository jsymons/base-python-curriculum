# Get All the Movies

Search the 'marvel' movie table in the database using `sqlite3` and return a list of all the movies in it.  

[Movie Spreadsheet](https://docs.google.com/spreadsheets/d/177aVH1m4kliVPFeZyL_M49xFu1nTlAj29xmZgDQ045Q/edit?usp=sharing)

Example:

```python
result = get_all_movies('marvel')
print(result[0]) # (1, 'Iron Man', 'Jon Favreau', 94, 79))
```