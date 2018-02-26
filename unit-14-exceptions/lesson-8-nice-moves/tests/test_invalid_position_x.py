import pytest


def test_invalid_position_x():
    with pytest.raises(InvalidPositionException):
        validate_tic_tac_toe_move('X', 5, 0)