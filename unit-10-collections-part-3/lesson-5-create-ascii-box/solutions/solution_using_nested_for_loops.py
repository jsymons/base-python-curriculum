def create_box(height, width, char):
    result = ''
    for h in range(height):
        line = ''
        for w in range(width):
            line += char
        result += (line + '\n')
    return result
