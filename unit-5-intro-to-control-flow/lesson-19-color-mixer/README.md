# Color mixer

Define a function `color_mixer` that receives two colors `color1` and `color2` 
and returns the color resulting from mixing them in EITHER ORDER. 
The colors received are either `red`, `blue`, or `yellow` and you should return:

`Magenta` if the colors mixed are `red` and `blue`

`Green` if the colors mixed are `blue` and `yellow`

`Orange` if the colors mixed are `yellow` and `red`


Examples:

```python
>>> color_mixer('red', 'blue')
'Magenta'
>>> color_mixer('blue', 'red')
'Magenta'
>>> color_mixer('blue', 'yellow')
'Green'
>>> color_mixer('yellow', 'red')
'Orange'
```
