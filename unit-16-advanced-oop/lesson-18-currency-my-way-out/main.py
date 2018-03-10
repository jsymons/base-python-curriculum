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

    def __init__(self, value, unit="USD"):
        pass

    def convert(self, target_unit):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __sub__(self, other):
        # Optional. Not tested
        pass

    def __isub__(self, other):
        # Optional. Not tested
        pass

    def __rsub__(self, other):
        # Optional. Not tested
        pass
