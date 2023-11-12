
import numpy as np

from agents.game_utils import BoardPiece, PlayerAction, SavedState, NO_PLAYER
from typing import Optional, Callable


def generate_move_random(board: np.ndarray, 
                         player: BoardPiece, 
                         saved_state: Optional[SavedState]) -> tuple[PlayerAction, Optional[SavedState]]:
    # Choose a valid, non-full column randomly and return it as `action`
    valid_moves = get_valid_moves(board)
    action = np.random.choice(valid_moves)
    return action, saved_state

def get_valid_moves(board: np.ndarray):
    is_open = board[-1, :] == NO_PLAYER
    valid_moves = np.arange(board.shape[1])[is_open]
    return valid_moves