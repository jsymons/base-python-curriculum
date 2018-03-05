def test_play():
    l = Lottery(numbers=[9])
    assert l.play(1) is False
    assert l.play(9) is True
