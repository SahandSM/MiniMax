
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


def iterate_states(board,depth):
    # where to copy?
    # what to return?
    # assing the return or not?
    # board_copy = np.copy(board)
    if depth == 0: # depth =0 means there has been x=depth moves carried out
        print(f'\depth 0 and board is:\n',pretty_print_board(board))
        return

    for move in range(2):
        new_board = board.copy()
        new_board = apply_player_action(new_board,move,2)
        depth0(new_board,depth-1)


