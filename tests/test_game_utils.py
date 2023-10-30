
from ..game_utils import initialize_game_state
def test_board_shape():
    assert initialize_game_state().shape ==  (6,7)