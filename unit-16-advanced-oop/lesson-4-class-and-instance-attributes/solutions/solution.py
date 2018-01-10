class Cookie(object):
    DEFAULT_SCARF_COLOR = 'Green'
    DEFAULT_BUTTON_COLOR = 'Blue'

    def __init__(self, scarf_color=None, buttons_color=None):
        self.scarf_color = scarf_color or self.DEFAULT_SCARF_COLOR
        self.buttons_color = buttons_color or self.DEFAULT_BUTTON_COLOR
