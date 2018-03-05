class NoTemperatureException(Exception):
    pass

class TempConverter:
    def __init__(self, fahrenheit=None, celsius=None):
        if not fahrenheit and not celsius:
            raise NoTemperatureException()
        self.temp_fahrenheit = fahrenheit
        self.temp_celsius = celsius
        
    def to_celsius(self):
        if self.temp_celsius:
            return self.temp_celsius
        return round((self.temp_fahrenheit - 32) * 5/9, 1)

    def to_fahrenheit(self):
        if self.temp_fahrenheit:
            return self.temp_fahrenheit
        return round((self.temp_celsius * 9/5) + 32, 1)