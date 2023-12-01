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

def test_is_open_col():
    board_string = ''' 
     - - - - - - - 
    |        O    |
    |        O    |
    |        O    |
    |O O   X X X  |
    |X O   X O X  |
    |X X O X O O X|
     - - - - - - -
    0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    is_open = is_open_col(board)
    print(is_open)
    return

def test_get_valid_moves():
    board_string = ''' 
     - - - - - - - 
    |        O    |
    |        O    |
    |        O    |
    |O O   X X X  |
    |X O   X O X  |
    |X X O X O O X|
     - - - - - - -
    0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    valid_moves = get_valid_moves(board)
    print(valid_moves)
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
    # board_copy = board.copy() it is not necessary if you are suare you are making a copy in the agent before applying actions there
    score = iterate_states(board)
    print('\nOriginal\n'
        ,pretty_print_board(board))
    print('score is :',score)
    return

def test_get_best_move():
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
    # board_copy = board.copy() it is not necessary if you are suare you are making a copy in the agent before applying actions there
    best_move, best_eval = get_best_move(board)
    print('best columns to take is:',best_move,
          f'best board score is:', best_eval)
    return


    