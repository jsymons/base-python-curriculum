BOARD_TEMPLATE = """
{0}  |  {1}  |  {2}
--------------
{3}  |  {4}  |  {5}
--------------
{6}  |  {7}  |  {8}
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    return BOARD_TEMPLATE.format(
        first_row[0], first_row[1], first_row[2],
        second_row[0], second_row[1], second_row[2],
        third_row[0], third_row[1], third_row[2],
    )
