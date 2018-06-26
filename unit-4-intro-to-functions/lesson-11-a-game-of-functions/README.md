A function is just an entity that takes care of processing input and turning it into some desired output.

```python
Input > Function > Output
```

For example, we can think about a function `add`, that receives two numbers and returns the sum of it:

```python
add(2, 3)  # 5
add(7, 5)  # 12
```

In our previous examples, we can see the input of the function being passed surrounded by parenthesis after the name of the function: `add(2, 3)`. This is the standard way of invoking a function in Python.

There are already functions builtin into the python language that we use all the time. For example, you already know about `print`. `print` takes a given string and prints it out in the screen. What's the output of print? Well, in this case is *nothing*. We say it's "void", "empty" or just "nothing", and in Python, it's represented with `None`:

```
print("Hello World")  # None
```

We just don't care about the output of print.

Another popular function is `len`. It returns the length of a string. Try it out by yourself:

```python
len("hello world") # 11
len("Python") # 6
```

In this case we see a "profound" change made by this function. It received a `string` and it returned an `int`!

## Defining your own functions (cheat sheet)

A function is defined in this way:

```python
def add(x, y):
    return x + y
```

1. `def` is a reserved keyword and **MUST** be used to start the definition of a function
2. `add` in this case is the name of the function. You can name them whatever you want. It's of course important to give good, meaningful names.
3. `x, y` are the parameters received for your function. You have to think carefully about the "input" of your function. What it receives. 

**Quick note here:** Even if you don't realize it, you're surrounded by "functions" and you constantly think about them. For example, what do you need to "start your car"? You probably need the car keys. The input is the car key and the output is the car running. What do you need to make a payment with your card? The input taking your card close to the sensor and sometimes a "password", and the output is the result of the transaction.

4. The body. Below the `def add(x, y):` you can start defining the body of the function. You can put as many lines as you want, but they **MUST** be indented four spaces to the right.

5. The `return` statement. This is **INCREDIBLY IMPORTANT**. It's the output of your function. It's that final think you want to produce as the result of it.

## Invoking functions

A function is "used" ("invoked", "called" are other verbs we use for the same action) in this way:

```python
res = add(2, 3)
print(res)  # 5


print(add(7, 5))  # 12
```

A few important notes:

1. For example, in `res = add(2, 3)`, we're assigning the result of the function `add(2, 3)` to the variable `res`. The function `add` **RETURNED** something. That value returned is assigned to `res`.

2. You can skip the assignment and pass it directly to another function. That's what happens with `print(add(7, 5))`. The result of `add(7, 5)` is immediately passed to `print`. We're "chaining" functions.
