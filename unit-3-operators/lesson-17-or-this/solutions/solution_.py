var1 = True and False
var2 = None is None
var3 = not True

# Use `or` to check if var1 or var3 evaluate to True
result1 = var1 or var3

# Now use two `or`s to combine all three variables and use `not`s to make the result evaluate to False
result2 = var1 or not var2 or var3
