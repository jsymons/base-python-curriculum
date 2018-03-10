# Going the Distance

Complete the methods for the class `Distance` so that it has functionality to compare different distances.

For the `convert_to_meters` method, the formula is multiplying the object's value * it's unit conversion (in the conversion dictionary at the top).

Use https://rszalski.github.io/magicmethods/ for magic method guidance, and read the tests if you get stuck.

```python
d1 = Distance(4, "ft")
d2 = Distance(1)
d3 = Distance(1000, "mm")

list_of_distances =[d1, d2]

print(d1) = "4ft"
print(list_of_distances) == '[Distance: 4ft, Distance: 1m]'

d1 == d3 # True
d1 != d2 # True
d1 > d2 # True
d2 < d1 # True
d1 <= d3 # True
d1 >= d3 # False
```