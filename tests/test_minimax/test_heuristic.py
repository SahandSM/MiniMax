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

    row_window, position = pivot_row(board,pivot)
    print('row_to_extract:',row_window)
    print('position:',position)


def test_pivot_col():
    board = np.arange(1,43).reshape(6,7)
    print('\n',board)

    pivot = (2,3)
    print(pivot)

    print(board[pivot])

    col_window, position = pivot_col(board,pivot)
    print('col_to_extract:',col_window)
    print('position:',position)


def test_pivot_diag():
    board = np.arange(1,43).reshape(6,7)
    print('\n',board)

    pivot = (2,3)
    print(pivot)

    print(board[pivot])

    diag_window, position = pivot_diag(board,pivot)
    print('daig_to_extract:',diag_window)
    print('position:',position)

def test_pivot_opp_diag():
    board = np.arange(1,43).reshape(6,7)
    print('\n',board)

    pivot = (2,3)
    print(pivot)

    print(board[pivot])

    opp_daig_window, position = pivot_opp_diag(board,pivot)
    print(opp_daig_window)
    print(position)

def test_evaluate_window_player_pieces():
    
    window = [1,0,1,1]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_window_player_pieces(window,player)
    print('window score player peices:',window_score)


def test_evaluate_window_opponent_pieces():
    
    window = [2,0,0,2]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_window_opponent_pieces(window,player)
    print('window score opponent peices:',window_score)


def test_evaluate_single_direction():
    # This is an example where evaluate_single_directin returns 
    # a score of 2 instead of 3 when we have the break line 
    row_window = [0,1,1,0,1,2,2]
    position = 3
    windows = [
        [0,1,1,0],
        [1,1,0,1],
        [1,0,1,1],
        [0,1,1,2]
    ]

    player = PLAYER1
    print('\nplayer:',player)

    direction_score = evaluate_single_direction(windows,player)
    print('direction score:',direction_score)

