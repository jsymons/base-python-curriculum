def test_create_1_cookies():
    cookies = Cookie.create_cookies(1)
    assert len(cookies) == 1

    cookie_1 = cookies[0]
    assert isinstance(cookie_1, Cookie)
