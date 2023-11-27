
import numpy as np

from agents.game_utils import *
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


def minimiax_move(board,depth):
    board_copy = board.copy()

    if depth>0:
        board_copy = apply_player_action(board_copy,6,2)
        minimiax_move(board_copy,depth-1)
    return board_copy
