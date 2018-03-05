def test_random_range():
    l = Lottery()
    assert l.get_answer() is not None
    assert l.play(l.get_answer()) is True