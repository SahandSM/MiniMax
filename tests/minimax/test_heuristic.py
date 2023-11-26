import numpy as np

from agents.agent_minimax import *

def test_WinChance_horz()
    board = np.array([[1,1,1,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]])
    horz_WinChance = WinChance_horz(board,1)

    assert horz_WinChance == 1