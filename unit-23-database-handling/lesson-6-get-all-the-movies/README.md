# Get All the Movies

Search the 'marvel' movie table in the database using `sqlite3` and return a list of all the movies in it. The `db` parameter is the db_connection that is setup in the table setup.

[Movie Spreadsheet](https://docs.google.com/spreadsheets/d/177aVH1m4kliVPFeZyL_M49xFu1nTlAj29xmZgDQ045Q/edit?usp=sharing)

Example:

```python
result = get_all_movies(db)
print(result[0]) # (1, 'Iron Man', 'Jon Favreau', 94, 79))
```