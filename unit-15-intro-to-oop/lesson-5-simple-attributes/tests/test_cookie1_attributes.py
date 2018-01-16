
def test_cookie1_attributes():
    assert isinstance(cookie1, Cookie) is True, 'cookie1 is not created'
    assert isinstance(cookie1, object) is True

    assert hasattr(cookie1, 'scarf') is True, "cookie1 doesn't have a scarf attribute"
    assert cookie1.scarf == 'green', "Cookie1's scarf isn't green"
