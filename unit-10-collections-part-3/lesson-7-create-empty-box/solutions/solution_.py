def create_empty_box(height, width, char):
    result = ''

    if height < 3 or width < 3:
        return "Invalid box dimensions"

    # Build line for top/bottom of box
    top_bottom_line = ''
    for w in range(width):
        top_bottom_line += char
    top_bottom_line += '\n'

    # Build line for middle of box
    middle_line = ''
    middle_line += char
    for w in range(1, width - 1):
        middle_line += ' '
    middle_line += char
    middle_line += '\n'

    # Build top of box
    result += top_bottom_line

    # Build middle of box
    for w in range(1, height -1):
        result += middle_line

    # Build bottom of box
    result += top_bottom_line

    return result