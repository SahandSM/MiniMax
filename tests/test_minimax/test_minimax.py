import numpy as np

from agents.game_utils import *
from agents.agent_minimax.minimax import *


def test_minimax_1():
    board_string = ''' 
    - - - - - - - 
    |             |
    |             |
    |        O    |
    |O O   X X X  |
    |X O   X O X  |
    |X X O X O O X|
    - - - - - - -
    0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    return

def test_iterate_states():
    board_string = ''' 
    - - - - - - - 
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    - - - - - - -
    0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    board_copy = board.copy()
    depth0(board_copy,2)
    print('\nOriginal\n'
        ,pretty_print_board(board))
    print('Copy\n'
        ,pretty_print_board(board_copy))
    return


    