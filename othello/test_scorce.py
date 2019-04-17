from board import Board
from move import Move
from ai import AI
from player import Player
from scorce import Scorce


def test_constructor():
    board = Board()
    move = Move(board)
    player = Player(move)
    ai = AI(move)
    scorce = Scorce(board, player, ai)
    assert scorce.board is board
    assert scorce.ai is ai
    assert scorce.player is player
    assert scorce.count_white == 0
    assert scorce.count_black == 0


def test_end_game():
    board = Board()
    move = Move(board)
    player = Player(move)
    ai = AI(move)
    scorce = Scorce(board, player, ai)
    if scorce.player.end_move():
        if not scorce.ai.move.get_valid_moves('w'):
            assert scorce.end_game()
    else:
        assert not scorce.end_game()


def test_draw_score_board():
    board = Board()
    move = Move(board)
    player = Player(move)
    ai = AI(move)
    scorce = Scorce(board, player, ai)
    for i in range(8):
        for j in range(8):
            board.array[i][j] = "b"
    for x in range(8):
        for y in range(8):
            if scorce.board.array[x][y] == "w":
                scorce.count_white += 1
            elif scorce.board.array[x][y] == "b":
                scorce.count_black += 1
    assert scorce.count_white == 0
    assert scorce.count_black == 64
