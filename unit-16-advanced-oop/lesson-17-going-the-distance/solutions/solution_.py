class Distance(object):
    METER_CONVERSIONS = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344
    }

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit

    def convert_to_meters(self):
        return self.value * self.METER_CONVERSIONS[self.unit]

    def __str__(self):
        return "{}{}".format(self.value, self.unit)

    def __repr__(self):
        return "Distance: {}{}".format(self.value, self.unit)

    def __eq__(self, other):
        if self.convert_to_meters() == other.convert_to_meters():
            return True
        return False

    def __ne__(self, other):
        if self.convert_to_meters() != other.convert_to_meters():
            return True
        return False

    def __lt__(self, other):
        if self.convert_to_meters() < other.convert_to_meters():
            return True
        return False

    def __le__(self, other):
        if self.convert_to_meters() <= other.convert_to_meters():
            return True
        return False

    def __gt__(self, other):
        if self.convert_to_meters() > other.convert_to_meters():
            return True
        return False

    def __ge__(self, other):
        if self.convert_to_meters() >= other.convert_to_meters():
            return True
        return False
