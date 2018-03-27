# Get Best and Worst Movies

Search the 'marvel' movie table in the database to find the best or worst movies.

The function should receive 4 parameters: 
* `table_name` - 'marvel' for the table name
* `rating_type` - choose 'tomatoes' or 'metacritic' to rank by one of these ratings
* `order_dir` - either 'ASC' or 'DESC' for the order of your results (DESC is best movies, ASC is worst)
* `limit` - how many results to return

We only want to select the title of the movie and the rating we are searching for.

[Movie Spreadsheet](https://docs.google.com/spreadsheets/d/177aVH1m4kliVPFeZyL_M49xFu1nTlAj29xmZgDQ045Q/edit?usp=sharing)

Example:

```python
result = get_best_and_worst_movies('marvel', 'metacritic', 'DESC', limit=3)

print(result[0]) # ('Black Panther', 88)
print(result[4]) # ('Thor: Ragnarok', 74)
```