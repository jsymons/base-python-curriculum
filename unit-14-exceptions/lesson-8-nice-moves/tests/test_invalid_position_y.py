import pytest


def test_invalid_position_y():
    with pytest.raises(InvalidPositionException):
        validate_tic_tac_toe_move('X', 0, 4)