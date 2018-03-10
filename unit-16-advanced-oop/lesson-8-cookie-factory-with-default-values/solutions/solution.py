class Cookie(object):
    DEFAULT_SCARF_COLOR = 'Green'
    DEFAULT_BUTTON_COLOR = 'Blue'

    def __init__(self, scarf_color, buttons_color):
        self.scarf_color = scarf_color
        self.buttons_color = buttons_color

    @classmethod
    def create_cookies(cls, amount, scarf_color=None, buttons_color=None):
        cookies = []
        for _ in range(amount):
            # cookies.append(Cookie())
            cookies.append(cls(
                scarf_color or cls.DEFAULT_SCARF_COLOR,
                buttons_color or cls.DEFAULT_BUTTON_COLOR))

        return cookies
