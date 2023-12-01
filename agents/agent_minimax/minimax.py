
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
    
def iterate_states(board,depth,player = True, i=np.array([0])):

    if depth == 0: # depth =0 means there has been x=depth moves carried out
        board_score = evaluate(i)
        print(f'\ndepth 0 reached for {i}:',
              f'\nboard score is: {board_score}\n',
              pretty_print_board(board))
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
    
def get_best_move(board,depth):
    best_move = None
    best_eval = -100

    for move in range(2):
        new_board = board.copy()
        new_board = apply_player_action(new_board, move, 2)
        eval = iterate_states(new_board, depth-1, False)  # Adjust depth as needed
        if eval > best_eval:
            best_eval = eval
            best_move = move

    return best_move
    
def evaluate(i):
    if i == [0]:
        return 0
    if i == [1]:
        return 1
    if i == [2]:
        return 2
    if i == [3]:
        return 3
    if i == [4]:
        return 0
    if i == [5]:
        return -1
    if i == [6]:
        return -1
    if i == [7]:
        return -2


