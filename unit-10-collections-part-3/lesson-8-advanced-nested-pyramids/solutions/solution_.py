def advanced_nested_pyramid(height, char, order):
    pyramid = ''

    for level in range(1, height + 1):
        row = ''
        if order == 'ASC':
            range_limit = level
        else:
            range_limit = height - level + 1

        for c in range(range_limit):
            row += char

        row += '\n'
        pyramid += row

    return pyramid
