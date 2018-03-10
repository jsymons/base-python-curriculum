
def test_factory_passing_only_scarf_color():
    cookies = Cookie.create_cookies(3, scarf_color='red')
    assert len(cookies) == 3
    cookie_1 = cookies[0]
    cookie_2 = cookies[1]
    cookie_3 = cookies[2]

    # All with the same scarf color
    assert cookie_1.scarf_color == 'red'
    assert cookie_2.scarf_color == 'red'
    assert cookie_3.scarf_color == 'red'

    # All with the same buttons color
    assert cookie_1.buttons_color == 'Blue'
    assert cookie_2.buttons_color == 'Blue'
    assert cookie_3.buttons_color == 'Blue'
