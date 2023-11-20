
import numpy as np

from agents.game_utils import initialize_game_state, pretty_print_board ,string_to_board, connected_four, check_end_state

def test_board_display():
    # displayed_board= []  

    # def mock_display(row):  
    #     displayed_board.append(f'{row}') 

    boardtest = np.zeros((3,7))
    boardtest[0,::2] = 1
    boardtest[1,::2] = 2
    boardtest[1,1::2] = 1
    boardtest[2,1::2] = 2

    printed_board = pretty_print_board(boardtest)

    # boardpirnttest_row0 = "| O O O |"
    # boardpirnttest_row1 = "|OXOXOXO|"
    # boardpirnttest_row2 = "|X X X X|"


    # assert (len(displayed_board) == boardtest.shape[0]
    #         and displayed_board[0] == boardpirnttest_row0  
    #         and displayed_board[1] == boardpirnttest_row1  
    #         and displayed_board[2] == boardpirnttest_row2
    #         )
    assert printed_board == '''
    | O O O |
    |OXOXOXO|
    |X X X X|
    '''
