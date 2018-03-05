class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def slope(self):
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        
    def y_intercept(self):
        m = self.slope()
        return self.p1.y - (m * self.p1.x)
    
    def formula(self):
        tpl = 'y = {m}x + {b:g}'
        m = self.slope()
        if m == 1:
            m = ''
        return tpl.format(m=m, b=self.y_intercept())
        