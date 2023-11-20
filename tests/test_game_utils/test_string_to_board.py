
import numpy as np

from agents.game_utils import *

def test_string_to_board():

    boardtest = np.array([[1., 0., 1., 0., 1., 0., 1.],
                            [2., 1., 2., 1., 2., 1., 2.],
                            [0., 2., 0., 2., 0., 2., 0.]])

    board_string = pretty_print_board(boardtest)

    board_array = string_to_board(board_string)

    assert(np.all(board_array == boardtest))
