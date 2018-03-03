# Country Methods

In your main module (at the right) we have defined a class `Country` and we've already created two instances: `usa` and `canada` with three attributes for each instance:

* `population`
* `area_in_km2` (in square kilometers)
* `gdp` (Gross domestic product in dollars)

Your job is to implement the following methods for the `Country` class:

_(**Important:** Tests are rounding numbers to avoid decimal issues)_

**Population density**
`population_density()` should return the number of inhabitants per square km. (`population / area`)

```python
usa.population_density()  # 33.12
canada.population_density()  # 3.52
```

**Dynamic area method**

Area can be expressed in different units. These instances have area expressed in _square kilometers_ but you can also use _square miles_ or even _Acres_ or _Hectares_.

The method `area()` of the class country should receive an **optional** parameter `unit` that can be either: `km2`, `mi2`, `acres`, `hectares`. By default, `units` is `km2`. If the unit passed is invalid (not one in the previous list) it should raise an `InvalidAreaUnitException` (that **you must** define). Examples:

```python
usa.area(unit='km2')  # 9833520
usa.area()            # 9833520 (same result, km2 is default)
usa.area(unit='mi2')  #
usa.area(unit='acres')  #
usa.area(unit='hectares')  #

usa.area(unit='INVALID UNIT')  # will raise InvalidAreaUnitException
```
For simplicity, use the following conversion table (based in km2):
```
1km2 => 0.3861 mi2
1km2 => 247 acres
1km2 => 100 hectares
```

**GDP per capita**
It's not our intention to talk politics, but we want to know how evenly distributed wealth is in each country. Define a method `gdp_per_capita()` that returns the _GDP per capita_ (`gdp / population`).

```python
usa.gdp_per_capita()
canada.gdp_per_capita()
```
