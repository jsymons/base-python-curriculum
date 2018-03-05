def test_get_answer():
    l = Lottery(numbers=[9])
    assert l.get_answer() is not None
    assert l.get_answer() == 9