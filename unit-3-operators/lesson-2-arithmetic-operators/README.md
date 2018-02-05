
# Arithmetic Operators

> _(Access this Jupyter Notebook using [this link](https://github.com/rmotr-curriculum/base-python-curriculum/blob/master/unit-3-operators/lesson-2-arithmetic-operators/Arithmetic%20Operators.ipynb))_

Arithmetic Operators will let you perform simple mathematical-like operations. The most intuitive use case is with numbers, but they'll also work with several other type like strings or collections.

These are the most common ones:


```python
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)  # 5² == 5 * 5
```

    7
    3
    10
    2.5
    25


But we also have a few less-common but equally important:

**Floor Division**

(Also known as Integer Division)


```python
print(5 // 2)
print(4 // 2)
```

    2
    2


**Modulus**

(Also known as "the remainder")


```python
print(4 % 2)
print(5 % 2)
print(10 % 2)
print(11 % 2)
```

    0
    1
    0
    1


## Arity of arithmetic operators

As you saw in the introduction, some of these operators will work as both **binary** and **unary** operators. Both the _minus_ (`-`) and _plus_ (`+`) symbols fall in this category:


```python
print(+3)
print(-5)

x = 2
print(+x)
print(-x)
```

    3
    -5
    2
    -2
