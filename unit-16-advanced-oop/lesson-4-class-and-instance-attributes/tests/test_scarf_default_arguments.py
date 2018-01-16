def test_scarf_default_arguments():
    cookie = Cookie(buttons_color='Red')
    cookie.scarf_color == 'Green'  # from DEFAULT_SCARF_COLOR
    cookie.buttons_color == 'Red'
