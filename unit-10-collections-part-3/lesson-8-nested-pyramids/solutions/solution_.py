def nested_pyramid(height, char):
    pyramid = ''
    for level in range(1, height + 1):
        row = ''
        for c in range(level):
            row += char

        row += '\n'
        pyramid += row

    return pyramid
