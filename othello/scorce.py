from move import Move
from board import Board
import random


class Scorce:
    def __init__(self, board, player, ai):
        self.board = board
        self.player = player
        self.ai = ai
        self.count_white = 0
        self.count_black = 0

    def input(self, message=''):
        print(123)
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def end_game(self):
        if self.player.end_move():
            if not self.ai.move.get_valid_moves('w'):
                return True
        else:
            return False

    def draw_score_board(self):
        for x in range(8):
            for y in range(8):
                if self.board.array[x][y] == "w":
                    self.count_white += 1
                elif self.board.array[x][y] == "b":
                    self.count_black += 1

        w = "white scorce: " + str(self.count_white)
        b = "black scorce: "+str(self.count_black)
        noLoop()
        if self.count_white == self.count_black:
            s = "Tied!"
        elif self.count_white > self.count_black:
            s = "White Won!"
        elif self.count_white < self.count_black:
            s = "Black Won!"
        t = "GAME OVER"

        fill(1, 0.7, 0.01)
        noStroke()
        rect(250, 200, 350, 300, 18)
        textSize(28)
        fill(1)
        text(t, 320, 270)
        text(w, 320, 390)
        text(b, 320, 450)
        text(s, 320, 330)

    def record_score(self):
        result = []
        current = []
        answer = self.input('enter your name: ')
        current.append(str(answer))
        current.append(int(self.count_black))
        f = open("scores.txt", 'r+')
        for line in f.readlines():
            line = line.strip()
            player_record = line.split()
            player_record[1] = int(player_record[1])
            player_record = tuple(player_record)
            result.append(player_record)
        result.append(tuple(current))
        result.sort(key=lambda tup: tup[1], reverse=True)
        f = open("scores.txt", 'w').close()
        f = open("scores.txt", 'w')
        for tul in result:
            f.write(str(tul[0]))
            f.write(' ')
            f.write(str(tul[1]))
            f.write('\n')
        f.close()
