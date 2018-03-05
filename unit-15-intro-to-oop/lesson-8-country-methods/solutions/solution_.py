class InvalidAreaUnitException(Exception):
    pass


class Country(object):
    def population_density(self):
        return float(self.population) / self.area_in_km2

    def gdp_per_capita(self):
        return float(self.total_gdp) / self.population

    def area(self, unit='km2'):
        if unit == 'km2':
            return self.area_in_km2
        elif unit == 'mi2':
            return self.area_in_km2 * 0.3861
        elif unit == 'acres':
            return self.area_in_km2 * 247
        elif unit == 'hectares':
            return self.area_in_km2 * 100
        else:
            raise InvalidAreaUnitException()


# vv Don't change these objects vv
usa = Country()
usa.name = 'United States of America'
usa.population = 325719178  # 325,719,178
usa.area_in_km2 = 9833520  # 9,833,520 km2
usa.total_gdp = 20199000000000  # 20.199 trillion

canada = Country()
canada.name = 'Canada'
canada.population = 35151728  # 35,151,728
canada.area_in_km2 = 9984670  # 9,984,670 km2
canada.total_gdp = 1836000000000  # 1.836 trillion
# ^^ Don't change these objects ^^
