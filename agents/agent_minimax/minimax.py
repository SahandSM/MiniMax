
import numpy as np

from agents.game_utils import *
from agents.agent_minimax.heuristic import *
from typing import Optional, Callable


def generate_move_minimax(board: np.ndarray, 
                         player: BoardPiece, 
                         saved_state: Optional[SavedState]) -> tuple[PlayerAction, Optional[SavedState]]:
    # return action, saved_state
    pass

def get_valid_moves(board: np.ndarray):
    is_open = board[-1, :] == 0
    valid_moves = np.arange(board.shape[1])[is_open]
    return valid_moves

def is_open_row(board):
    is_open = board[-1, :] == 0
    return is_open

def get_free_row(board):
    # remember to check for legal moves first.
    free_row = [np.count_nonzero(board[:,i]) for i in range(7)]
    return free_row


def iterate_states_0(board,depth,player = True):
    # where to copy?
    # assing the return or not?
        # what to return?
    if depth == 0: # depth =0 means there has been x=depth moves carried out
        print(f'\depth 0 and board is:\n',pretty_print_board(board))
        return

    if player == True:
        for move in range(2):
            new_board = board.copy() # copy should be done inside the loop becasue ... don't move it out
            new_board = apply_player_action(new_board,move,2)
            iterate_states(new_board,depth-1,False)
    else:
        for move in range(2):
            new_board = board.copy() # copy should be done inside the loop becasue ... don't move it out
            new_board = apply_player_action(new_board,move,1)
            iterate_states(new_board,depth-1,True)
    
def iterate_states(board,depth,player = True, i=np.array([0])):
    # where to copy?
    # assing the return or not?
        # what to return?
    if depth == 0: # depth =0 means there has been x=depth moves carried out
        print(f'\ndepth 0 reached for {i}:\n',pretty_print_board(board))
        board_score = evaluate(i)
        i += 1
        return board_score

    if player == True:
        max_score = -100
        for move in range(2):
            new_board = board.copy() # copy should be done inside the loop becasue ... don't move it out
            new_board = apply_player_action(new_board,move,2)
            board_score = iterate_states(new_board,depth-1,False,i)
            max_score = max(max_score,board_score)
        return max_score
    else:
        min_score = +100
        for move in range(2):
            new_board = board.copy() # copy should be done inside the loop becasue ... don't move it out
            new_board = apply_player_action(new_board,move,1)
            board_score = iterate_states(new_board,depth-1,True,i)
            min_score = min(min_score,board_score)
        return min_score

def evaluate(i):
    if i == [0]:
        return 1
    if i == [1]:
        return 2
    if i == [2]:
        return 0
    if i == [3]:
        return -1

