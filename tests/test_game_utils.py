
import numpy as np

from agents.game_utils import initialize_game_state, pretty_print_board ,string_to_board, connected_four, check_end_state

def test_board_shape():
    assert initialize_game_state().shape ==  (6,7)

# def test_board_dtype():
#     assert initialize_game_state().dtype ==  np.int8

# def test_board_initials():
#     assert initialize_game_state().all() == 0


# # def test_board_display():
# #     displayed_board= []  

# #     def mock_display(row):  
# #         displayed_board.append(f'{row}') 

# #     boardtest = np.zeros((3,7))
# #     boardtest[0,::2] = 1
# #     boardtest[1,::2] = 2
# #     boardtest[1,1::2] = 1
# #     boardtest[2,1::2] = 2

# #     pretty_print_board(boardtest, mock_display)

# #     boardpirnttest_row0 = "| O O O |"
# #     boardpirnttest_row1 = "|OXOXOXO|"
# #     boardpirnttest_row2 = "|X X X X|"


#     assert (len(displayed_board) == boardtest.shape[0]
#             and displayed_board[0] == boardpirnttest_row0  
#             and displayed_board[1] == boardpirnttest_row1  
#             and displayed_board[2] == boardpirnttest_row2
#             )

# def test_conver_boardprint():
#     boardprint_inut = '| O O O | |OXOXOXO| |X X X X|'

#     boardprint_converted = string_to_board(boardprint_inut)

#     boardtest = np.zeros((3,7))
#     boardtest[0,::2] = 1
#     boardtest[1,::2] = 2
#     boardtest[1,1::2] = 1
#     boardtest[2,1::2] = 2

#     assert(np.all(boardprint_converted == boardtest))

# def test_action():
#        board = np.array([[1,1,1,1,1,1,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0]])
#        board_original = apply_player_action(board,7,PLAYER1)
#        assert np.all(board - board_original == np.array([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1]]))

# def test_connected_not():
#     board = np.array([[1,1,1,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,1,0,1,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]])
#     player =1
#     assert connected_four(board,1) == False

# def test_connected_hor():
#     board = np.array([[1,1,1,1,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,1,0,1,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]])
#     player =1
#     assert connected_four(board,1) == True

# def test_connected_ver():
#     board = np.array([[1,1,1,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,1,0,1,0,1],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]])
#     player =1
#     assert connected_four(board,1) == True

# def test_connected_diagp():
#     board = np.array([[1,1,1,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,1,0,0,1],[0,0,1,0,0,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]])
#     player =1
#     assert connected_four(board,1) == True

# def test_connected_diagn():
#     board = np.array([[1,1,1,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,1,0,0,1],[0,0,0,0,1,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]])
#     player =1
#     assert connected_four(board,1) == True

# def test_draw():
#     displayed_state = []

#     def mock_display(Gstate):  
#         displayed_state.append(Gstate)

#     board = np.arange(1,43).reshape(6,7)

#     check_end_state(board,1,mock_display)
#     assert displayed_state == ['IS_DRAW']

# def test_win():
#     displayed_state = []

#     def mock_display(Gstate):  
#         displayed_state.append(Gstate)

#     board = np.array([[1,1,1,1,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,1,0,1,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]])

#     check_end_state(board,1,mock_display)
#     assert displayed_state == ['IS_WIN']

# def test_still_playing():
#     displayed_state = []

#     def mock_display(Gstate):  
#         displayed_state.append(Gstate)

#     board = np.array([[1,1,1,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,1,0,1,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]])

#     check_end_state(board,1,mock_display)
#     assert displayed_state == ['STILL_PLAYING']

# test_board_shape()
# test_board_dtype()
# test_board_initials()
# test_board_display()
# test_conver_boardprint()
# test_connected_not()
# test_connected_hor()
# test_connected_ver()
# test_connected_diagp()
# test_connected_diagn()
# test_draw()
# test_win()
# test_still_playing()
