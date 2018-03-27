import sqlite3

def get_all_movies(table_name):
    result = []
    for row in db.execute('SELECT * FROM %s;', (table_name,)):
        result.append(row)
    return result