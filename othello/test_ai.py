from board import Board
from move import Move
from ai import AI


def test_constructor():
    board = Board()
    move = Move(board)
    ai = AI(move)
    assert ai.move is move


def test_do_move():
    board = Board()
    move = Move(board)
    ai = AI(move)
    assert ai.do_move()

    for i in range(6):
        for j in range(6):
            board.array[i][j] = "b"
    assert not ai.do_move()


def test_bestchoice():
    board = Board()
    move = Move(board)
    ai = AI(move)
    board.array[3][2] = "b"
    board.array[3][3] = "b"
    board.array[3][4] = "b"
    board.array[4][3] = "b"
    board.array[4][4] = "w"
    ai.bestchoice()
    assert board.array[3][2] == board.array[3][4] == board.array[4][3] == "b"
    assert board.array[3][3] == board.array[4][4] == board.array[2][2] == "w"
