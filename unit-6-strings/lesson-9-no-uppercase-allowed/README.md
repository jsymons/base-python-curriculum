# No Uppercase Allowed

Complete the function `neutralize_uppercase` so that it returns `stringy` the same as it was received if there are no capital letters in it or an empty string "" if there were. You need to use a while loop to go through each letter of the string one at a time to check for uppercase letters.

Examples:

```python
# String has no uppercase letters so returns input string unchanged
>>>  neutralize_uppercase("snitch") == "snitch"
'snitch'

# String has uppercase letters so returns empty string
>>>  neutralize_uppercase("eXpelliarMus")
''
```

Hint: You'll probably need to use len() to figure out your condition to stop looping through the string. You'll also need to use upper().