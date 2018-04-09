# Cow Says Moo

Extend the `Animal` class with three different subclasses: `Cow`, `Sheep`, and `Fox`.

When each animal is created, it should receive a name as a parameter. Rather than having a `talk` method in each subclass, you can just put one `talk` method in the parent `Animal` class and have the subclasses use that.

The talk method should say "[Animal_name] says [Animal_sound]"

Each subclass should have a `sound` attribute for that particular animal.

* The sound for `Cow` is `"moo"`
* The sound for `Sheep` is `"baaaaa"`
* The sound for `Fox` is `"Ring-ding-ding-ding-dingeringeding"`

Try and take advantage of the `super` keyword in the subclasses for the `__init__` method (the `Animal` class should only store the attribute `name`, but the subclasses also store the attribute `sound`).

Example:

```python
sheep = Sheep("Baaab")
print(sheep.sound) # baaaaa
print(sheep.talk()) # Baaab says baaaaa
```
