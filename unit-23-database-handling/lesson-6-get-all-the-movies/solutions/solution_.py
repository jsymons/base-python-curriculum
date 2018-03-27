import sqlite3

def get_all_movies(table_name):
    result = []
    params = ['table_name']
    for row in db.execute('SELECT * FROM ?;', params):
        result.append(row)
    return result