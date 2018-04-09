class Shape(object):
    def area(self):
        raise NotImplementedError()


class Circle(Shape):
    pass


class Rectangle(Shape):
    pass


class Square(Rectangle):
    # Only __init__ method
    pass
