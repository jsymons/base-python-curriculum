import random


class Lottery(object):
    def __init__(self, numbers=None):
        if numbers is None:
            numbers = range(0, 50)
        self.answer = random.choice(numbers)
        
    def get_answer(self):
        return self.answer

    def play(self, number):
        if self.answer == number:
            return True
        return False