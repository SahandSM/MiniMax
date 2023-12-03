import numpy as np

from agents.agent_minimax.heuristic import *

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