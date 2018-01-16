# Cookie Factory with default values

Extend the previous example `create_cookies` to receive two optional parameters (`scarf_color` and `buttons_color`). If they're not included, `DEFAULT_SCARF_COLOR` and `DEFAULT_BUTTON_COLOR` class attributes should be used. Example:

```python
cookies = Cookie.create_cookies(5, scarf_color='Red', buttons_color='Yellow')
[<Cookie obj>, <Cookie obj>, <Cookie obj>, <Cookie obj>, <Cookie obj>]
# these cookies should have scarf_color == 'Red' and buttons_color == 'Yellow'

cookies = Cookie.create_cookies(3)
[<Cookie obj>, <Cookie obj>, <Cookie obj>]
# these cookies should have scarf_color == 'Green' and buttons_color == 'Blue'
```
