def test_best_movies():
    result = get_best_and_worst_movies(db, 'metacritic', 'DESC')
    assert len(result) == 5
    assert result[0] == ('Black Panther', 88)
    assert result[4] == ('Thor: Ragnarok', 74)
