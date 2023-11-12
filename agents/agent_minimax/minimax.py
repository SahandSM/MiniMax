
import numpy as np

from agents.game_utils import apply_player_action, connected_four, BoardPiece, PlayerAction, SavedState, NO_PLAYER
from typing import Optional, Callable


def generate_move_minimax(board: np.ndarray, 
                         player: BoardPiece, 
                         saved_state: Optional[SavedState]) -> tuple[PlayerAction, Optional[SavedState]]:
    valid_moves = get_valid_moves(board)

    action, is_win = get_winning_move(board,player,valid_moves)
    if not is_win:
        print('choosing randomly: ',valid_moves)
        action = np.random.choice(valid_moves)

    return action, saved_state

def get_winning_move(board:np.ndarray, player: BoardPiece, valid_moves: np.ndarray):
    is_win = False
    action = []
    for column in valid_moves:
        borad_inspect_move = board.copy()
        borad_inspect_move = apply_player_action(borad_inspect_move, column, player)
        print('checking win:', column)
        is_win = connected_four(borad_inspect_move, player)
        print('is win?', is_win)
        if is_win:
            action = column
            return action , is_win
    return action, is_win

def get_valid_moves(board: np.ndarray):
    is_open = board[-1, :] == NO_PLAYER
    valid_moves = np.arange(board.shape[1])[is_open]
    print('checking valid moves: ', valid_moves)
    return valid_moves
