# Nice Moves

Complete the function `validate_tic_tac_toe_move` that receives inputs `symbol`, `position_x`, and `position_y` for a move in Tic Tac Toe and checks to make sure each of them are valid.

There are no builtin python exceptions that describe these exceptions meaningfully if one of these move inputs are invalid, so you'll need to create two custom exceptions: InvalidSymbolException and InvalidPositionException.

Remember, all you have to do to create a custom exception is the following:

```python
class ExceptionNameHere(Exception):
    pass
```

You'll learn more about what the keywords class and Exception mean later. You leave the keyword pass in because all we need to do is raise the exception.


For this function, do the following:
Raise InvalidSymbolException if the `symbol` is not an 'X' or 'O'
Raise InvalidPositionException if the `position_x` or `position_y` are not 0, 1, or 2.

Examples:

```python
validate_tic_tac_toe_move('J', 0, 1) # Raises InvalidSymbolException
validate_tic_tac_toe_move('X', 0, 4) # Raises InvalidPositionException
validate_tic_tac_toe_move('X', 7, 0) # Raises InvalidPositionException
validate_tic_tac_toe_move('O', 1, 2) # Does not raise any exceptions
```