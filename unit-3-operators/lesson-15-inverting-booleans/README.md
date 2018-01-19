# Inverting Booleans

There are a lot of different ways of writing the same code to accomplish something.

To demonstrate this, let's take a look at booleans.

You can either check that something is `False` or, if you are sure that it is a boolean, you can check if it is `not` `True`. Same thing, right?

```python
variable = False

# Two ways of doing the same thing
print(variable is False) # True
print(not variable) # True
# Note that the second way uses less code so it is preferred

# Inverting a boolean
true_variable = True
variable = not true_variable 
print(variable) # False
```

Use the not operator to check for the opposite of something in the following code!
