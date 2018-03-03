class Car(object):
    def __init__(self, electric):
        self.electric = electric

    def drive(self):
        if self.electric:
            return 'WHIRRRRRRR'
        return 'VROOOOM'
