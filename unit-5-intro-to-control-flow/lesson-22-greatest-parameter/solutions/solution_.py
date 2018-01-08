def greatest_parameter(a, b, c, d, e):
    greatest = a

    if b > a:
        greatest = b

    if c > greatest:
        greatest = c

    if d > greatest:
        greatest = d

    if e > greatest:
        greatest = e

    return greatest
