class Shape(object):
    def area(self):
        raise NotImplementedError()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(side, side)
