# Identity Matrix

An identity matrix is defined in the following way: 

![image](https://user-images.githubusercontent.com/872296/33191804-a8ae391a-d09b-11e7-99aa-f6d3e29635f6.png)

Basically, all the elements in the diagonal are ones (`1`s) and the rest are zeros (`0`s).

An identity matrix has a `size` associated. For example, this is an identity matrix of size 3:

```
1 0 0
0 1 0
0 0 1
```


And this is a matrix of size 5:

```
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
```

A matrix is represented, Pythonically, with a "list of lists". Example:

```python
# size 3
size_3_matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
# size 5
size_5_matrix = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]
```

Write a function `identity_matrix` that receives a `size` parameter and builds an identity matrix using "lists of lists".
