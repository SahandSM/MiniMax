



def test_heuristic():
    board_string = ''' 
    - - - - - - - 
    |             |
    |             |
    |        O    |
    |O O   X X X  |
    |X O   X O X  |
    |X X O X O O X|
    - - - - - - -
    0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    return

def test_heuristic():
    board_copy = minimiax_move(board,3)
    print('Original'
        ,pretty_print_board(board))
    print('Copy'
        ,pretty_print_board(board_copy))
    return
