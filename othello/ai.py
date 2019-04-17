from board import Board
from move import Move


class AI:
    def __init__(self, move):
        self.move = move
        self.board_weights = [
            [120, -20, 20,  5,  5,  20, -20, 120],
            [-20, -40, -5, -5, -5,  -5, -40, -20],
            [20,   -5, 15,  3,  3,  15,  -5,  20],
            [5,    -5,  3,  3,  3,   3,  -5,   5],
            [5,    -5,  3,  3,  3,   3, -5,   5],
            [20,   -5, 15,  3,  3,  15, -5,  20],
            [-20, -40, -5, -5, -5,  -5, -40, -20],
            [120, -20, 20,  5,  5,  20, -20, 120]
        ]

    def do_move(self):
        if not self.move.get_valid_moves('w'):
            return False
        else:
            return True

    def bestchoice(self):
        sorce = []
        if not self.move.get_valid_moves('w'):
            return False
        else:
            action_list = self.move.get_valid_moves('w')
            best = action_list[0]
            for action in action_list:
                sorce.append(self.board_weights[action[0]][action[1]])
                if self.board_weights[action[0]][action[1]] > self.board_weights[best[0]][best[1]]:
                    best = action
            x = best[0]
            y = best[1]
            self.move.make_move(x, y, 'w')
