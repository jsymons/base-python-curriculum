# Lottery Time

Create a class called `Lottery` with that optionally receives a list  `numbers` containing the possible winning numbers. If `numbers` is not received as an optional argument, set it to be a list ranging from 0-49. When created, your Lottery object should have an attribute `answer` created that is _random_ number from the `numbers` list.

It needs to have two methods:
- `get_answer` that returns the answer variable for that object
- `play` that receives a number and returns True if the number matches the answer and False otherwise

Example:

```python
l = Lottery(numbers=[9])
l.get_answer() # 9
l.play(1) # False
l.play(9) # True
```


