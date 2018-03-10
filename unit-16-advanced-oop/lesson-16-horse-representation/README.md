# Horse Representation

Horses are more than just objects. Please give them some string and machine representation using magic methods.

The `Horse` class should accept two attributes, name and breed.

Use the following examples to make `__str__` and `__repr__` magic methods to produce similar outputs.

Examples:

```python
talking_horse = Horse("Mr. Ed", "Saddlebred")
sparkles = Horse("Charlie", "Unicorn")

team_horse_squad = [talking_horse, sparkles]

print(sparkles) # "Charlie the Unicorn"
print(talking_horse) # "Mr. Ed the Saddlebred"

print(team_horse_squad) # '[Horse: Mr. Ed, Saddlebred, Horse: Charlie, Unicorn]'
```