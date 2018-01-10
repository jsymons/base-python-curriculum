def test_buttons_default_arguments():
    cookie = Cookie(scarf_color='Red')
    cookie.scarf_color == 'Red'
    cookie.buttons_color == 'Blue'  # from DEFAULT_BUTTON_COLOR
