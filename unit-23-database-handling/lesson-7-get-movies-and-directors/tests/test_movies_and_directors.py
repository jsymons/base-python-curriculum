def test_movies_and_directors():
    result = get_movies_and_directors(db, limit=3)
    assert len(result) == 3
    assert result[0] == ('Iron Man', 'Jon Favreau')
    assert result[2] == ('Iron Man 2', 'Jon Favreau')
