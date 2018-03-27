def test_worst_movies():
    result = get_best_and_worst_movies(db, 'tomatoes', 'ASC', limit=3)
    assert len(result) == 3
    assert result[0] == ('Thor: The Dark World', 66)
    assert result[1] == ('The Incredible Hulk', 67)
    assert result[2] == ('Iron Man 2', 73)
