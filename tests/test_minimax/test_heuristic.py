import numpy as np

from agents.agent_minimax.heuristic import *

def test_heuristic_1():
    #use this array to test functions in heuristic module
    board = np.arange(1,43).reshape(6,7)
    print(board)

    pivot_point = (4,2)
    print(board[pivot_point])
    return


def test_heuristic_2():
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
    print(board_string)
    print(board)

    pivot = (2,3)
    print(pivot)

    player = 2

    score = evaluate_at_pivot(board,pivot,player)
    print(score)

def test_extract_windows():
    array = [2,2,0,1,1,1,0]
    pivot = 5
    windows = extract_windows(array,pivot)
    print(windows)

def test_pivot_row():
    board = np.arange(1,43).reshape(6,7)
    print('\n',board)

    pivot = (2,3)
    print(pivot)

    print(board[pivot])

    array_window, position = pivot_row(board,pivot)
    print(array_window)
    print(position)



