def test_create_5_cookies():
    cookies = Cookie.create_cookies(5)
    assert len(cookies) == 5

    cookie_1 = cookies[0]
    cookie_2 = cookies[1]
    cookie_3 = cookies[2]
    cookie_4 = cookies[3]
    cookie_5 = cookies[4]

    assert isinstance(cookie_1, Cookie)
    assert isinstance(cookie_2, Cookie)
    assert isinstance(cookie_3, Cookie)
    assert isinstance(cookie_4, Cookie)
    assert isinstance(cookie_5, Cookie)
