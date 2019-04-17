from board import Board
from move import Move


class Player:
    def __init__(self, move):
        self.move = move

    def do_move(self):
        x = mouseX
        y = mouseY
        x = x//100
        y = y//100
        if self.move.valid_move(x, y) and self.move.tiles_to_flip(x, y, 'b'):
            return True
        else:
            return False

    def make_move(self):
        x = mouseX
        y = mouseY
        x = x//100
        y = y//100
        self.move.make_move(x, y, 'b')

    def end_move(self):
        if self.move.get_valid_moves('b'):
            return False
        else:
            return True
