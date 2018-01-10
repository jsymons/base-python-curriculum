# Class and Instance Attributes

Extend the `Cookie` class from the previous assignment. This time, the `Cookie` constructor should accept two parameters when it's initialized (`scarf_color` and `buttons_color`). Both attributes should be optional. When the Cookie is constructed, if any of the parameters are missing, use the `DEFAULT_BUTTON_COLOR` and `DEFAULT_SCARF_COLOR` class attributes as default. Example:

```python
c1 = Cookie(scarf_color='Red', buttons_color='Yellow')
c1.scarf_color == 'Red'
c1.buttons_color == 'Yellow'

c2 = Cookie(scarf_color='Red')
c2.scarf_color == 'Red'
c2.buttons_color == 'Blue'  # from DEFAULT_BUTTON_COLOR

c3 = Cookie(buttons_color='Red')
c3.scarf_color == 'Green'  # from DEFAULT_SCARF_COLOR
c3.buttons_color == 'Red'

c4 = Cookie()
c4.scarf_color == 'Green'  # from DEFAULT_SCARF_COLOR
c4.buttons_color == 'Blue'  # from DEFAULT_BUTTON_COLOR
```
