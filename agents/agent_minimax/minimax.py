
import numpy as np

from agents.game_utils import BoardPiece, PlayerAction, SavedState, NO_PLAYER
from typing import Optional, Callable


def generate_move_random(board: np.ndarray, 
                         player: BoardPiece, 
                         saved_state: Optional[SavedState]) -> tuple[PlayerAction, Optional[SavedState]]:
    