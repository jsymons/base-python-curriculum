class Loan(object):
    def __init__(self, value):
        self.value = value

class Movie(object):
    def __init__(self, price):
        self.price = price

class Milk(object):
    def __init__(self, cost):
        self.cost = cost


def calculate(p1, p2):
    total = 0
    for product in [p1, p2]:
        for attr in ['cost', 'price', 'value']:
            if hasattr(product, attr):
                total += getattr(product, attr)
    return total
