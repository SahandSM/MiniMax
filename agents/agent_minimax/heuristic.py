import numpy as np

def WinChance_horz(board, player):
    pass

def next_row(board):

    free_row = [np.count_nonzero(board[:,i]) for i in range(7)]

    return free_row

    
    