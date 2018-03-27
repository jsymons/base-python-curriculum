import sqlite3

def get_best_and_worst_movies(table_name, rating_type, order_dir, limit=5):
    result = []
    params = {
      'table_name': 'marvel',
      'rating_type': 'metacritic',
      'order_dir': 'DESC',
      'limit': 5
    }

    for row in db.execute('SELECT title, :rating_type FROM :table_name ORDER BY :rating_type :order_dir LIMIT :limit;', params):
        result.append(row)
    return result