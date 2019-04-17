from board import Board

def test_constructor():
    board = Board()
    assert board.array[3][3] == "w"
    assert board.array[3][4] == "b"       
    assert board.array[4][3] == "b"
    assert board.array[4][4] == "w"