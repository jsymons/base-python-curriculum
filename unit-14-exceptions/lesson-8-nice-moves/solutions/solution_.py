# Define InvalidSymbolException here
class InvalidSymbolException(Exception):
    pass

# Define InvalidPositionException here
class InvalidPositionException(Exception):
    pass


def validate_tic_tac_toe_move(symbol, position_x, position_y):
    if symbol not in ('X', 'O'):
        raise InvalidSymbolException()

    valid_positions = (0, 1, 2)  # could have used range(0, 3)
    if position_x not in valid_positions or position_y not in valid_positions:
        raise InvalidPositionException()