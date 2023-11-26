
import numpy as np

from agents.game_utils import *

def test_action():
    board = np.array([
                    [1,1,1,1,1,1,1],
                    [0,0,0,0,0,0,1],
                    [0,0,0,0,0,0,1],
                    [0,0,0,0,0,0,1],
                    [0,0,0,0,0,0,1],
                    [0,0,0,0,0,0,0]])

    board_action_applied = apply_player_action(board,6,PLAYER1)
    assert np.all(board_action_applied == np.array([[1,1,1,1,1,1,1],
                                                    [0,0,0,0,0,0,1],
                                                    [0,0,0,0,0,0,1],
                                                    [0,0,0,0,0,0,1],
                                                    [0,0,0,0,0,0,1],
                                                    [0,0,0,0,0,0,1]]))

def test_connected_not():
    board = np.array([[1,1,1,0,0,0,1],
                      [0,0,0,0,0,0,1],
                      [0,0,0,0,0,0,1],
                      [0,0,1,0,1,0,0],
                      [0,1,0,0,0,1,0],
                      [1,0,0,0,0,0,1]])
    player =1
    assert connected_four(board,1) == False

def test_connected_hor():
    board = np.array([[1,1,1,1,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,1,0,1,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]])
    player =1
    assert connected_four(board,1) == True

def test_connected_ver():
    board = np.array([[1,1,1,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,1,0,1,0,1],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]])
    player =1
    assert connected_four(board,1) == True

def test_connected_diagp():
    board = np.array([[1,1,1,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,1,0,0,1],[0,0,1,0,0,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]])
    player =1
    assert connected_four(board,1) == True

def test_connected_diagn():
    board = np.array([[1,1,1,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,1,0,0,1],[0,0,0,0,1,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]])
    player =1
    assert connected_four(board,1) == True

def test_draw():
    board = np.arange(1,43).reshape(6,7)

    CheckedState = check_end_state(board,1)
    assert CheckedState == GameState.IS_DRAW

def test_win():
    board = np.array([[1,1,1,1,0,0,1],
                      [0,0,0,0,0,0,1],
                      [0,0,0,0,0,0,1],
                      [0,0,1,0,1,0,0],
                      [0,1,0,0,0,1,0],
                      [1,0,0,0,0,0,1]])

    CheckedState = check_end_state(board,1)
    assert CheckedState == GameState.IS_WIN

def test_still_playing():
    board = np.array([[1,1,1,0,0,0,1],
                      [0,0,0,0,0,0,1],
                      [0,0,0,0,0,0,1],
                      [0,0,1,0,1,0,0],
                      [0,1,0,0,0,1,0],
                      [1,0,0,0,0,0,1]])

    CheckedState = check_end_state(board,1)
    assert CheckedState == GameState.STILL_PLAYING