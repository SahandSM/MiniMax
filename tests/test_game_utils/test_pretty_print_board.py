
import numpy as np

from game_utils import *

def test_pretty_print_board():

   boardtest = np.array([[1., 0., 1., 0., 1., 0., 1.],
                         [2., 1., 2., 1., 2., 1., 2.],
                         [0., 2., 0., 2., 0., 2., 0.]])

   printed_board = pretty_print_board(boardtest)
    
   assert printed_board ==''' - - - - - - - 
|  O   O   O  |
|O X O X O X O|
|X   X   X   X|
 - - - - - - -
 0 1 2 3 4 5 6'''
