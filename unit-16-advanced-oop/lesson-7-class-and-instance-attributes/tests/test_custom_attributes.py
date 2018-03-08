def test_custom_attributes():
    cookie = Cookie(scarf_color='Red', buttons_color='Yellow')
    cookie.scarf_color == 'Red'
    cookie.buttons_color == 'Yellow'
