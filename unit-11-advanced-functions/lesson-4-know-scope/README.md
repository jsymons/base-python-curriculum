# Know Scope

Analyze the following code and answer:
What will be the final value of `c` after the execution of this code:

```python
a = 10
b = 3
c = 7
def test_scope(b):
    a = 11
    return a + b + c

c = c + test_scope(5)

whats_the_value_of_c = ?
```

Give your answer in the editor:
