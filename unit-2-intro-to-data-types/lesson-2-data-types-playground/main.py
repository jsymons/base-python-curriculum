from decimal import Decimal

print("===== Integers =====")
x = 5
print(type(x))
y = int('2')
print(x * y)

print("===== Floats =====")
f = 0.1
print(f * 3)

print("===== Decimals =====")
d = Decimal('0.1')
print(d * 3)

print("===== Booleans =====")
b1 = False
b2 = not b1
print(b1)
print(b2)

print("===== None =====")

n = None
print(n)
print(n is None)
