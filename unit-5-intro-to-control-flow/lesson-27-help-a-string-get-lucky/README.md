# Help a String Get Lucky

Use a while loop to complete the function `get_lucky` so that it receives a string `poor_string` and an integer `lucky_number` as a parameter. Add "7" to `poor_string` an amount of times equal to `lucky_number` and return the result.

Examples:

```python
>>>  get_lucky("rabbit foot", 3)
'rabbit foot777'

>>>  get_lucky("shiny penny", 5)
'shiny penny77777'
```

Hint: You can use the `+=` operator to concatenate new stuff to strings.

Another Hint: You might need to keep track of how many times you've added the string "7" somewhere. And watch out for those infinite loops. They're dangerous!

Daft Punk was absolutely not playing during the creation of this assignment.