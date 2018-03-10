# Attribute Guessing

Today you have the privilege of creating a terrible attribute guessing game for objects! You won't always know if an attribute exists when you are working with objects, so it's good practice to learn how to dynamically check and get data from them. 

In this game, you will search possible hiding places in a `Location` for prizes. The winning hiding places will stored as attributes in the `Location` object, and you have to correctly guess them to get your prizes.

Create a class `Location` that receives a dictionary of hiding places as keys with prizes as values. When an object is created, store the dictionary key-value pairs as attributes within the object.

Then create a `search` method that receives a list of guesses as strings and returns a list of prizes for correct attribute guesses. Go through the list of guesses and if an attribute has the same name as the guess string, add the prize (the value for that attribute) to the list of prizes. Return that prize list after checking all the guess strings.


Example:

```python
house = Location({
    'dresser': 'socks',
    'pantry': 'cake',
    'safe': 'money'
})

house.search(['basement', 'closet', 'bed', 'dresser']) # returns prize list ['socks'] 
```
