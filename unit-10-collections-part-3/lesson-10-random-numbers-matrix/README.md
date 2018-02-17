# Random Numbers Matrix

Use the `random` module (more below) to write a function `random_matrix` that returns a matrix size `m` × `n` with random numbers (`m` is the number of rows and `n` is the number of columns).
**The only restriction is that elements in the matrix CAN'T be repeated**, they must be unique. Examples:

```python
random_matrix(3, 2)
[
    [29, 11],
    [91, 85],
    [56, 18],
]

random_matrix(4, 4)
[
    [29, 11, 23, 90],
    [91, 85, 92, 75],
    [56, 18, 13, 47],
    [65, 99, 49, 10]
]
```

### Random Numbers
To generate random numbers you can use the `random` module. It's super simple, check the following example ([or try it for yourself](https://repl.it/repls/StarchyRunnyAmericanrobin)):

```python
import random
number = random.randint(0, 100) # A random number between 0 and 100
print(number)
```
