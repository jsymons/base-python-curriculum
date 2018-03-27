import sqlite3

def get_movies_and_directors(db, table_name, limit=5):
    result = []
    params = [table_name, limit]
    for row in db.execute('SELECT title, director FROM ? LIMIT ?;', params):
        result.append(row)
    return result