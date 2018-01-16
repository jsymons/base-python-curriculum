def test_format_empty_board():
    """
    This is the board used in this test:
        X  |  O  |  -
        --------------
        O  |  -  |  -
        --------------
        O  |  -  |  X
    """
    first_row = 'XO-'
    second_row = 'O--'
    third_row = 'O-X'
    expected_board = """
X  |  O  |  -
--------------
O  |  -  |  -
--------------
O  |  -  |  X
"""
    board = format_tic_tac_toe_board(first_row, second_row, third_row)

    assert board == expected_board
