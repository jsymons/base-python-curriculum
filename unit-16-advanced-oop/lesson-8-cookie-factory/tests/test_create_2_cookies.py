def test_create_2_cookies():
    cookies = Cookie.create_cookies(2)
    assert len(cookies) == 2

    cookie_1 = cookies[0]
    cookie_2 = cookies[1]
    assert isinstance(cookie_1, Cookie)
    assert isinstance(cookie_2, Cookie)
