import pytest


def test_invalid_symbol():
    with pytest.raises(InvalidSymbolException):
        validate_tic_tac_toe_move('J', 0, 1)