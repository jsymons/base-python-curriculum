def test_get_movies():
    assert db is not None
    result = get_all_movies(db)
    assert result[0] == (1, 'Iron Man', 'Jon Favreau', 94, 79)
    assert result[1] == (2, 'The Incredible Hulk', 'Louis Leterrier', 67, 61)
    assert result[17] == (18, 'Black Panther', 'Ryan Coogler', 97, 88)
