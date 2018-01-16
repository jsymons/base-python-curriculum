def color_mixer(color1, color2):
    if color1 == 'blue':
        if color2 == 'red':
            return 'Magenta'
        elif color2 == 'yellow':
            return 'Green'
    elif color1 == 'red':
        if color2 == 'yellow':
            return 'Orange'
        elif color2 == 'blue':
            return 'Magenta'
    elif color1 == 'yellow':
        if color2 == 'blue':
            return 'Green'
        elif color2 == 'red':
            return 'Orange'
