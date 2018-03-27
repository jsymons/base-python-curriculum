import sqlite3
db = sqlite3.connect("file::memory:?cache=shared")

db.executescript("""

drop table if exists marvel;
create table marvel (
  id integer primary key autoincrement,
  title text not null,
  director text not null,
  tomatoes integer,
  metacritic integer
);

-- marvel
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (1, 'Iron Man', 'Jon Favreau', 94, 79);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (2, 'The Incredible Hulk', 'Louis Leterrier', 67, 61);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (3, 'Iron Man 2', 'Jon Favreau', 73, 57);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (4, 'Thor', 'Kenneth Branagh', 77, 57);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (5, 'Captain America: The First Avenger', 'Joe Johnston', 80, 66);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (6, 'Marvels The Avengers', 'Joss Whedon', 92, 69);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (7, 'Iron Man 3', 'Shane Black', 80, 62);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (8, 'Thor: The Dark World', 'Alan Taylor', 66, 54);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (9, 'Captain America: The Winter Soldier', 'Anthony and Joe Russo', 89, 70);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (10, 'Guardians of the Galaxy', 'James Gunn', 91, 76);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (11, 'Avengers: Age of Ultron', 'Joss Whedon', 75, 66);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (12, 'Ant-Man', 'Peyton Reed', 82, 64);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (13, 'Captain America: Civil War', 'Anthony and Joe Russo', 91, 75);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (14, 'Doctor Strange', 'Scott Derrickson', 89, 72);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (15, 'Guardians of the Galaxy Vol. 2', 'James Gunn', 83, 67);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (16, 'Spider-Man: Homecoming', 'Jon Watts', 92, 73);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (17, 'Thor: Ragnarok', 'Taika Waititi', 92, 74);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (18, 'Black Panther', 'Ryan Coogler', 97, 88);
""")


def get_movies_and_directors(db, limit=5):
    query = 'SELECT title, director FROM marvel LIMIT :limit'
    cursor = db.execute(query, {
        'limit': limit
    })
    return cursor.fetchall()
