import numpy as np
import cProfile

from agents.agent_minimax.heuristic import *
from agents.agent_minimax.minimax import *

# python -m Profiling.profile_minimax

board_string = ''' 
 - - - - - - - 
|             |
|             |
|             |
|             |
|      O      |
|      X X    |
 - - - - - - -
 0 1 2 3 4 5 6
'''
board = string_to_board(board_string)
print('\n',board)

player = PLAYER1

cProfile.run(
'evaluate_board(board,player)','profiling/evaluate_board_profile.prof'
)

cProfile.run(
    'generate_move_minimax(board,player,None)','profiling/generate_move_minimax_profile.prof'
)