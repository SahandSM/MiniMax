
import numpy as np

from agents.game_utils import BoardPiece, PlayerAction, SavedState, NO_PLAYER
from typing import Optional, Callable


def generate_move_random(board: np.ndarray, 
                         player: BoardPiece, 
                         saved_state: Optional[SavedState]) -> tuple[PlayerAction, Optional[SavedState]]:
    # Choose a valid, non-full column randomly and return it as `action`
    is_valid_move = False
    while not is_valid_move:
        action = np.random.randint(0, 6)
        try:
            is_valid_move = handle_illegal_moves(board, action)
        except TypeError:
            print('Not the right format, try an integer.')
        except IndexError:
            print('Selected integer is not in the range of possible columns (0 - 6).')
        except ValueError:
            print('Selected column is full.')

    return action, saved_state

def handle_illegal_moves(board: np.ndarray, column: PlayerAction):
    try:
        column = PlayerAction(column)
    except:
        raise TypeError

    is_in_range = PlayerAction(0) <= column <= PlayerAction(6)
    if not is_in_range:
        raise IndexError

    is_open = board[-1, column] == NO_PLAYER
    if not is_open:
        raise ValueError

    return True