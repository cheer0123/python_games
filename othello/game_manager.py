from move import Move
from ai import AI
from player import Player


class GameManager:
    def __init__(self, player, ai):
        self.player = player
        self.ai = ai
        self.player_turn = True

    def turn(self):
        if self.player.do_move():
            self.player_turn = False
        elif self.player.end_move():
            self.player_turn = False
        else:
            self.player_turn = True
