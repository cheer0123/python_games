from board import Board
from move import Move
from ai import AI
from player import Player
from game_manager import GameManager


def test_constructor():
    board = Board()
    move = Move(board)
    player = Player(move)
    ai = AI(move)
    gc = GameManager(player, ai)
    assert ai.move is move
    assert player.move is move
    assert gc.ai is ai
    assert gc.player is player


def test_turn():
    board = Board()
    move = Move(board)
    player = Player(move)
    ai = AI(move)
    gc = GameManager(player, ai)

    if gc.player.end_move():
        assert not gc.player_turn
    else:
        assert gc.player_turn
