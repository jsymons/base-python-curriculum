def test_factory_passing_both_values():
    cookies = Cookie.create_cookies(
        5, scarf_color='red', buttons_color='yellow')
    assert len(cookies) == 5

    cookie_1 = cookies[0]
    cookie_2 = cookies[1]
    cookie_3 = cookies[2]
    cookie_4 = cookies[3]
    cookie_5 = cookies[4]

    # All with the same scarf color
    assert cookie_1.scarf_color == 'red'
    assert cookie_2.scarf_color == 'red'
    assert cookie_3.scarf_color == 'red'
    assert cookie_4.scarf_color == 'red'
    assert cookie_5.scarf_color == 'red'

    # All with the same buttons color
    assert cookie_1.buttons_color == 'yellow'
    assert cookie_2.buttons_color == 'yellow'
    assert cookie_3.buttons_color == 'yellow'
    assert cookie_4.buttons_color == 'yellow'
    assert cookie_5.buttons_color == 'yellow'
