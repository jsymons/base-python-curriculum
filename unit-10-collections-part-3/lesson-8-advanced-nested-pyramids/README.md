# Advanced Nested Pyramids

Extend your previous solution to include a third parameter "order" which can be either `"ASC"` or `"DESC`. Depending of the order provided, the pyramid will be displayed in ascending order (`"ASC"`) or descending order (`"DESC"`). Examples:

**A pyramid with 5 levels ASC:**
```python
nested_pyramid(5, '*', 'ASC')
*
**
****
*****
******
```

**A pyramid with 5 levels DESC:**
```python
nested_pyramid(5, '*', 'DESC')
*****
****
***
**
*
```

**A pyramid with 3 levels ASC:**
```python
nested_pyramid(5, '#', 'ASC')
#
##
###
```

**A pyramid with 3 levels DESC:**
```python
nested_pyramid(5, '@', 'DESC')
@@@
@@
@
```
