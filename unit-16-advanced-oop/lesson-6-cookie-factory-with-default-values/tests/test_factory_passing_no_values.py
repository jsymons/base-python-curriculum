def test_factory_passing_no_values():
    cookies = Cookie.create_cookies(4)  # No attributes passed
    assert len(cookies) == 4

    cookie_1 = cookies[0]
    cookie_2 = cookies[1]
    cookie_3 = cookies[2]
    cookie_4 = cookies[3]

    # All with the same scarf color
    assert cookie_1.scarf_color == 'Green'
    assert cookie_2.scarf_color == 'Green'
    assert cookie_3.scarf_color == 'Green'
    assert cookie_4.scarf_color == 'Green'

    # All with the same buttons color
    assert cookie_1.buttons_color == 'Blue'
    assert cookie_2.buttons_color == 'Blue'
    assert cookie_3.buttons_color == 'Blue'
    assert cookie_4.buttons_color == 'Blue'
