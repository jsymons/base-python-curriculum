def test_format_full_board():
    """
    This is the board used in this test:
        X  |  O  |  X
        --------------
        O  |  X  |  O
        --------------
        O  |  O  |  X
    """
    first_row = 'XOX'
    second_row = 'OXO'
    third_row = 'OOX'
    expected_board = """
X  |  O  |  X
--------------
O  |  X  |  O
--------------
O  |  O  |  X
"""
    board = format_tic_tac_toe_board(first_row, second_row, third_row)

    assert board == expected_board
