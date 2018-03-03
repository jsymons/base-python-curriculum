# Make a Car with Doors!

Create a class `Car` that is initialized by providing one mandatory argument: `color`.
It will also have one optional/default argument `'number_of_doors'` set to be 4 if it is not received as an argument.

Example:

```python
car1 = Car(color='blue', number_of_doors=2)
print(car1.color)  # 'blue'
print(car1.number_of_doors)  # 2

car2 = Car(color='green') # note that it is not passed `number_of_doors` argument
print(car2.color)  # 'green'
print(car2.number_of_doors)  # 4
```
