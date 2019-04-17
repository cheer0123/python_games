from board import Board
from move import Move
from player import Player


def test_constructor():
    board = Board()
    move = Move(board)
    player = Player(move)
    assert player.move is move


def test_end_move():
    board = Board()
    move = Move(board)
    player = Player(move)
    if player.move.get_valid_moves('b'):
        assert not player.end_move()
    else:
        assert player.end_move()
