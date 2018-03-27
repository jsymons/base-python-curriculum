# Get Movies and Directors

Search the 'marvel' movie table in the database and return the title and director from each movie. Only get as many movies as the limit parameter.

[Movie Spreadsheet](https://docs.google.com/spreadsheets/d/177aVH1m4kliVPFeZyL_M49xFu1nTlAj29xmZgDQ045Q/edit?usp=sharing)

Example:

```python
get_movies_and_directors('marvel', limit=3)

'''
[('Iron Man', 'Jon Favreau'), ('The Incredible Hulk', 'Louis Leterrier'),
    ('Iron Man 2', 'Jon Favreau')
]
'''
```