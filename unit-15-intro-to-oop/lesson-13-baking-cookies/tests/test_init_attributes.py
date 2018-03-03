def test_init_attributes():
    c1 = Cookie(scarf='green', buttons='blue')
    assert isinstance(c1, object) is True

    assert hasattr(c1, 'scarf') is True
    assert c1.scarf == 'green'

    assert hasattr(c1, 'buttons') is True
    assert c1.buttons == 'blue'

    assert hasattr(c1, 'hat') is True
    assert c1.hat is None
