class Currency(object):
    USD_CONVERSIONS = {
        'CHF': 0.95,
        'CAD': 1.28,
        'GBP': 0.72,
        'JPY': 106.80,
        'EUR': 0.81,
        'USD': 1.0,
        'MXN': 18.62,
        'ARG': 20.24,
        'AUD': 1.27
    }
    BASE_UNIT = 'USD'

    def __init__(self, value, unit="USD"):
        if unit not in self.USD_CONVERSIONS:
            raise ValueError('Invalid Unit {}'.format(unit))
        self.value = value
        self.unit = unit

    def convert(self, target_unit):
        if target_unit not in self.USD_CONVERSIONS:
            raise ValueError('Invalid Unit {}'.format(target_unit))
        self_usd = self.value / self.USD_CONVERSIONS[self.unit]
        target_usd = self_usd * self.USD_CONVERSIONS[target_unit]
        return Currency(round(target_usd, 4), target_unit)

    def __str__(self):
        return '{}${}'.format(self.unit, self.value)

    def __repr__(self):
        return "Currency({}, '{}')".format(self.value, self.unit)

    def __eq__(self, other):
        self_usd = self.convert(self.BASE_UNIT)
        other_usd = other.convert(self.BASE_UNIT)
        return self_usd.value == other_usd.value

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        self_usd = self.convert(self.BASE_UNIT)
        other_usd = other.convert(self.BASE_UNIT)
        return self_usd.value < other_usd.value

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return self > other or self == other

    def __add__(self, other):
        self_usd = self.convert(self.BASE_UNIT)
        other_usd = other.convert(self.BASE_UNIT)
        return Currency(self_usd.value + other_usd.value, self.BASE_UNIT)

    def __iadd__(self, other):
        total_usd = self + other
        total_self_unit = total_usd.convert(self.unit)
        return Currency(total_self_unit.value, self.unit)

    def __radd__(self, other):
        return self + Currency(other, 'USD')

    def __sub__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __rsub__(self, other):
        pass
