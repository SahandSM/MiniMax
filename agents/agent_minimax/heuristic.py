import numpy as np

from agents.game_utils import *
from typing import Optional, Callable
from typing import List, Tuple

def evaluate_board(board,player):
    all_pivots = get_pivots(board)
    all_pivot_scores_player, all_pivot_scores_opponent = evlaute_at_all_pivots(board,all_pivots,player)
    board_score = aggregate_scores(all_pivot_scores_player, all_pivot_scores_opponent)
    return board_score

def aggregate_scores(all_pivot_scores_player, all_pivot_scores_opponent):
    threes_player = all_pivot_scores_player.count(3)
    twos_player = all_pivot_scores_player.count(2)
    threes_opponent = all_pivot_scores_opponent.count(-3)
    twos_opponent = all_pivot_scores_opponent.count(-2)

    if threes_player > 1 and threes_opponent <= 1: board_score = 500
    elif threes_player <= 1 and threes_opponent > 1: board_score = -500
    else: board_score = (threes_player - threes_opponent) * 15 + \
                        (twos_player - twos_opponent) * 10
        
    return board_score
    

def evlaute_at_all_pivots(board,all_pivots,player):

    all_pivot_scores_player = []
    all_pivot_scores_opponent = []

    for pivot in all_pivots:
        pivot_score_player, pivot_score_opponent =  evaluate_at_pivot(board,pivot,player)      
        all_pivot_scores_player = all_pivot_scores_player + pivot_score_player
        all_pivot_scores_opponent = all_pivot_scores_opponent + pivot_score_opponent

    return all_pivot_scores_player, all_pivot_scores_opponent


def evaluate_at_pivot(board,pivot,player):
    '''returns an array of length 4 for each player. each element in the array refers to the evaluation at one axis.
    '''
    row_score_player, row_score_opponent = evaluate_row(board,pivot,player)
    col_score_player, col_score_opponent = evaluate_col(board,pivot,player)
    diag_score_player, diag_score_opponent  = evaluate_diag(board,pivot,player)
    opp_diag_score_player, opp_diag_score_opponent  = evaluate_opp_diag(board,pivot,player)

    pivot_score_player = row_score_player + col_score_player + diag_score_player + opp_diag_score_player
    pivot_score_opponent = row_score_opponent +col_score_opponent + diag_score_opponent +opp_diag_score_opponent
    
    return pivot_score_player, pivot_score_opponent

def evaluate_row(board,pivot_point,player):
    array,position = get_pivot_row(board,pivot_point)
    windows_row = extract_windows(array,position)
    row_score_player = evaluate_windows_player(windows_row,player)
    row_score_opponent = evaluate_windows_opponent(windows_row,player)
    return row_score_player,row_score_opponent

def get_pivot_row(board,pivot):
    """
    return the row contraining the pivot and the position of the pivot in the row.
    """
    row_window = board[pivot[0]]
    position = pivot[1]
    return row_window,position

def evaluate_col(board,pivot_point,player):
    array,position = get_pivot_col(board,pivot_point)
    windows_col = extract_windows(array,position)
    col_score_player = evaluate_windows_player(windows_col,player)
    col_score_opponent = evaluate_windows_opponent(windows_col,player)
    return col_score_player,col_score_opponent

def get_pivot_col(board,pivot):
    col_window = board[:,pivot[1]]
    position = pivot[0]
    return col_window,position

def evaluate_diag(board,pivot_point,player):
    array,position = get_pivot_diag(board,pivot_point)
    windows_diag = extract_windows(array,position)
    diag_score_player = evaluate_windows_player(windows_diag,player)
    diag_score_opponent = evaluate_windows_opponent(windows_diag,player)
    return diag_score_player,diag_score_opponent

def get_pivot_diag(board,pivot):
    diag_window = np.diag(board,pivot[1]-pivot[0])
    position = min(pivot)
    return diag_window,position

def evaluate_opp_diag(board,pivot_point,player):
    array,position = get_pivot_opp_diag(board,pivot_point)
    windows_opp_diag = extract_windows(array,position)
    opp_diag_score_player = evaluate_windows_player(windows_opp_diag,player)
    opp_diag_score_opponent = evaluate_windows_opponent(windows_opp_diag,player)
    return opp_diag_score_player,opp_diag_score_opponent

def get_pivot_opp_diag(board,pivot):
    borad_flipped = np.fliplr(board)
    pivot = pivot[0],6-pivot[1]
    opp_daig_window = np.diag(borad_flipped,pivot[1]-pivot[0])
    position = min(pivot)
    return opp_daig_window,position


def extract_windows(array: list,pivot_position: int) -> list:
    """
    Extracts a sliding window of size 4 from the given list 'array' centered around the 'pivot_position'.

    Parameters:
    - array (list): The input list from which windows are to be extracted.
    - pivot_position (int): The index around which the sliding window is centered.

    Returns:
    list: A list of sublists, each representing a sliding window of size 4 around the 'pivot_position'.
    
    Example:
    >>> array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> pivot_position = 4
    >>> extract_windows(array, pivot_position)
    [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
    """
    start = max(0,pivot_position-3)
    last_window = len(array)-3
    end = min(pivot_position+1,last_window)
    windows = []
    for w in range(start,end):
        window = list(array[w:w+4])
        windows.append(window)
    return windows

def evaluate_windows_player(windows: List[List[int]], player: int) -> List[int]:
    """
    Evaluate the score of multiple windows for the player.

    Parameters
    ----------
    windows : List[List[int]]
        A list of windows, where each window is a list of pieces on the game board.
    player : int
        The player for whom the windows are evaluated.

    Returns
    -------
    List[int]
        A list containing the maximum score among all evaluated windows for the specified player.
    """
    windows_score = [0]
    for window in windows:
        window_score = evaluate_single_window_player(window,player)
        windows_score = windows_score + window_score
    direction_score = [max(windows_score)]
    return direction_score

def evaluate_windows_opponent(windows: List[List[int]], player: int) -> List[int]:
    """
    Evaluate the score of multiple windows for the opponent player.

    Parameters
    ----------
    windows : List[List[int]]
        A list of windows, where each window is a list of pieces on the game board.
    player : int
        The opponent player for whom the windows are evaluated.

    Returns
    -------
    List[int]
        A list containing the minimum score among all evaluated windows for the opponent player.
    """
    windows_score = [0]
    for window in windows:
        window_score = evaluate_single_window_opponent(window,player)
        windows_score = windows_score + window_score
    direction_score = [min(windows_score)]
    return direction_score

def evaluate_single_window_player(window: List[int], player: int) -> List[int]:
    """
    Evaluate the score of a single window for the player/agent.

    Parameters
    ----------
    window : List[int]
        A window of pieces on the game board.
    player : int
        The player for whom the window is evaluated.

    Returns
    -------
    List[int]
        A list containing the score of the window for the specified player.
    """
    window_score = [0]
    n_pieces = window.count(player)
    n_zeros = window.count(0)

    if n_pieces == 3: window_score = [3]
    elif n_pieces == 2 and n_zeros == 2: window_score = [2]
    return window_score

def evaluate_single_window_opponent(window: List[int], player: int) -> List[int]:
    """
    Evaluate the score of a single window for the opponent player.

    Parameters
    ----------
    window : List[int]
        A window of pieces on the game board.
    player : int
        The player for whom the window is evaluated.

    Returns
    -------
    List[int]
        A list containing the score of the window for the opponent player.
    """
    window_score = [0]
    n_pieces = window.count(player)
    n_zeros = window.count(0)

    if n_pieces == 0 and n_zeros == 1: window_score = [-3]
    elif n_pieces == 0 and n_zeros == 2: window_score = [-2]
    return window_score

def get_pivots(board: np.ndarray) -> List[Tuple[int, int]]:
    """
    Get the coordinates of all available pivot positions in the board.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.

    Returns
    -------
    List[Tuple[int, int]]
        A list of (row, column) tuples representing the coordinates of available pivot positions.

    Notes
    -----
    The function considers only the top rows up to the maximum height calculated
    using the get_max_height function.
    """
    pivot_board = board.copy()

    max_height = get_max_height(pivot_board)

    max_heigh_pivot = pivot_board[:max_height+1,:]

    all_pivots = list(zip(*np.where(max_heigh_pivot == 0)))
    return all_pivots

def get_max_height(board: np.ndarray) -> int:
    """
    Get the maximum height among the free columns in the board.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.

    Returns
    -------
    int
        The maximum height among the free columns.
    """
    col_heights = [np.count_nonzero(board[:,i]) for i in range(BOARD_COLS)]
    col_heights = np.array(col_heights)
    is_open = is_open_row(board)
    free_col_heights = col_heights[is_open]
    max_height = max(free_col_heights)
    return max_height

def is_open_row(board: np.ndarray) -> bool:
    """
    Check if the last row of the board is open (does not contain any non-zero elements).

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.

    Returns
    -------
    bool
        True if the last row is open, False otherwise.
    """
    is_open = board[-1, :] == 0
    return is_open






    
    