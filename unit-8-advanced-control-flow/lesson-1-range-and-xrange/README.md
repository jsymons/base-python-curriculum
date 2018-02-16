### Understanding `range()`

Sometimes you don't need to iterate over a collection; but just a given number of times. For example, repeat 3 times a query to a database. Or perform 5 attempts to create a user. Your objective is to repeat something X times.

Technically, there's no _collection_ or _sequence_ involved, so given what we've learned up to this point, you could use a while loop.

Example: _Print `"Hello World"` 3 times._


```python
i = 0
while i < 3:
    print("Hello World")
    i += 1
```

    Hello World
    Hello World
    Hello World


But we know the problems of while loops, like the problem of infinite loops, and thinking about the condition, etc. **_There should be a better way._** And there is...

If we need to iterate 3 times, we could create a _dummy_ collection with only 3 elements and iterate over it. We'd not care about the elements in the collection, we just need them to be three:


```python
l = [1, 1, 1]
for elem in l:
    print("Hello World")
```

    Hello World
    Hello World
    Hello World



```python
l = [None, None, None]
for elem in l:
    print("Hello World")
```

    Hello World
    Hello World
    Hello World


We could even use strings:


```python
for elem in 'XYZ':
    print("Hello World")
```

    Hello World
    Hello World
    Hello World


With some magic added:


```python
for elem in 'X' * 3:
    print("Hello World")
```

    Hello World
    Hello World
    Hello World


All these options are performing the same operation and yielding the same result (printing "Hello World" 3 times), but using the much safer and convenient for loop instead of a while loop.

This option also allows us to use the given "number" provided in the collection. For example, if we need to print "Hello 1", "Hello 2", "Hello 3", etc, we can create a list with natural numbers. Example:


```python
l = [1, 2, 3]
for number in l:
    print("Hello {}".format(number))
```

    Hello 1
    Hello 2
    Hello 3


### Enter `range()`

The `range` python builtin function will simplify the process of creating these collections to iterate.

The only purpose of this function, is to create sequences with numbers. Examples:

```python
range(5)        # [0, 1, 2, 3, 4]
range(0, 5)     # [0, 1, 2, 3, 4]
range(1, 5)     # [1, 2, 3, 4]
range(2, 8)     # [2, 3, 4, 5, 6, 7]
range(2, 11, 2) # [2, 4, 6, 8, 10]
range(-5, -1)   # [-5, -4, -3, -2]
```

As you can see, it takes the usual parameters that we saw with slicing:

* `start` (optional, default `0`)
* `end`
* `step` (optional, default `1`)

So that means that we can use `range` to construct one of these lists for us to iterate. For example, to 3 times "Hello World", we can use `range(3)`. We don't care much about the contents, so we could even use `range(15, 18)`, although `range(3)` is a little bit more clear:


```python
for elem in range(3):
    print("Hello World")
```

    Hello World
    Hello World
    Hello World


We don't care about the content, so we could name `elem` anything else, like `i` or `x`. If you don't need that variable, a usual convention is to call it `_`, which is a valid variable name:



```python
_ = 'RMOTR'  # Valid variable name
print(_)
```

    RMOTR



```python
for _ in range(3):
    print("Hello World")
```

    Hello World
    Hello World
    Hello World


In our example of printing `"Hello 1"`, `"Hello 2"`, `"Hello 3"`, etc, we **DO** need the variable name. So we won't name it `_` in that case:



```python
for number in range(1, 4):  # I'm usinga different range now
    print("Hello {}".format(number))
```

    Hello 1
    Hello 2
    Hello 3


### Don't use `range` to manually access elements in a collection 😡

We're serious. We often see code like this:


```python
users = ['Jane', 'Mary', 'John']

for i in range(len(users)):
    user = users[i]
    print(user)
```

    Jane
    Mary
    John


**THIS IS WRONG ☠**

It's difficult to read and **highly inefficient**; and that's the whole purpose of a for loop. The same code is as simple as:


```python
users = ['Jane', 'Mary', 'John']

for user in users:
    print(user)
```

    Jane
    Mary
    John


So, as a rule of thumb. If you need to iterate over a collection `C` and you find yourself accessing individual elements by index from the collection `C` **inside** a for loop; you're probably doing something wrong. Just don't.

![How about no](https://imgflip.com/s/meme/How-About-No-Bear.jpg)

### Differences between Python 2 and Python 3

A few lines above I told you that `range` returned a **list** containing numbers specified by `start`, `end`, `step`... well, kind of...

In Python 3, `range` doesn't return "an actual list" anymore. It returns a **_"generator"_**. It's a more advanced concept, and **we'll learn about them during the course**. To see it in action, if you try running the following code in Python 3, you won't see an ACTUAL list, but something like `range(3, 10)`.


```python
range(3, 10)
```




    range(3, 10)



If you want a list, you need to "force" range be one by explicitly calling `list`:


```python
list(range(3, 10))
```




    [3, 4, 5, 6, 7, 8, 9]



Finally, Python 2 has two "range" functions; one called [`range`](https://docs.python.org/2/library/functions.html#range) and other called [`xrange`](https://docs.python.org/2/library/functions.html#xrange). In Python 2, `range` will actually return a list, but `xrange` behaves like Python3's version, returning a generator. So be aware of that.
