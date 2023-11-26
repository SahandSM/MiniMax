import numpy as np

from agents.agent_minimax import *

# def test_WinChance_horz():
#     board = np.array([[1,1,1,0,0,0,0],
#                       [0,0,0,0,0,0,0],
#                       [0,0,0,0,0,0,0],
#                       [0,0,0,0,0,0,0],
#                       [0,0,0,0,0,0,0],
#                       [0,0,0,0,0,0,0]])
#     horz_WinChance = WinChance_horz(board,1)

#     assert horz_WinChance == 1

def test_next_row():
    board = np.array([
                    [1,1,1,0,2,0,2],
                    [0,1,0,0,1,0,2],
                    [0,0,0,0,2,0,1],
                    [0,0,0,0,0,0,2],
                    [0,0,0,0,0,0,2],
                    [0,0,0,0,0,0,0]])
    
    free_row = next_row(board)
    assert free_row == [1,2,1,0,3,0,5]

    