def test_cookie2_attributes():
    assert isinstance(cookie2, Cookie) is True, 'cookie2 is not created'
    assert isinstance(cookie2, object) is True

    assert hasattr(cookie2, 'buttons') is True, "cookie2 doesn't have a scarf attribute"
    assert cookie2.buttons == 'blue', "Cookie2's scarf isn't blue"
