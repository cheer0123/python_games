from move import Move
from board import Board


def test_constructor():
    board = Board()
    move = Move(board)
    assert move.board is board


def test_is_on_board():
    board = Board()
    move = Move(board)
    assert move.is_on_board(1, 1)
    assert not move.is_on_board(8, 9)


def test_valid_move():
    board = Board()
    move = Move(board)
    assert move.valid_move(5, 5)
    assert not move.valid_move(4, 4)
    assert not move.valid_move(9, 4)


def test_tiles_to_flip():
    board = Board()
    move = Move(board)
    move.tiles_to_flip(3, 2, 'b')
    assert move.to_flip == [[3, 3]]
    assert not move.tiles_to_flip(3, 2, 'w')
    board.array[4][2] = "w"
    assert not move.tiles_to_flip(5, 1, 'b')

    # test tile at the corner of the board
    board.array[3][2] = "w"
    board.array[3][1] = "w"
    move.tiles_to_flip(3, 0, 'b')
    assert move.to_flip == [[3, 3], [3, 2], [3, 1]]


def test_make_move():
    board = Board()
    move = Move(board)
    board.array[3][2] = "w"
    board.array[3][1] = "w"
    move.make_move(3, 0, 'b')
    assert board.array[3][2] == board.array[3][1] == board.array[3][0] == "b"


def test_get_valid_moves():
    board = Board()
    move = Move(board)
    board.array[4][2] = "b"
    board.array[4][1] = "b"
    board.array[5][3] = "b"
    move.get_valid_moves('w')
    assert move.get_valid_moves('w') == [[2, 4], [3, 5], [
        4, 0], [5, 1], [6, 2], [6, 3]]

    for i in range(6):
        for j in range(6):
            board.array[i][j] = "w"
    assert not move.get_valid_moves('b')
