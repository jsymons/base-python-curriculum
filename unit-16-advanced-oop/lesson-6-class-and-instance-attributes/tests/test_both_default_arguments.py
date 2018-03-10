def test_both_default_arguments():
    cookie = Cookie()
    cookie.scarf_color == 'Green'  # from DEFAULT_SCARF_COLOR
    cookie.buttons_color == 'Blue'  # from DEFAULT_BUTTON_COLOR
