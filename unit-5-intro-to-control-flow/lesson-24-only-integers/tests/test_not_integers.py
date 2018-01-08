def test_not_integers():
    assert add_only_integers(2, 'what') == 'invalid parameters'
