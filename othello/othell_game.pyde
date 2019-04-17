from board import Board
from move import Move
from game_manager import  GameManager
from player import Player
from ai import AI
from scorce import Scorce

WIDTH =800
HEIGHT = 800
board = Board()
move = Move(board) 
player = Player(move)
ai = AI(move)
gm = GameManager(player, ai)
scorce = Scorce(board, player, ai)


current = player
startTime = 0
display_massage = None
DISPLAY_DURATION = 2000

def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)

def draw():
    global display_massage, startTime, DISPLAY_DURATION
    c = color(100, 100, 100)
    greenValue = green(c)
    background(0.23, 0.5, 0.15)
    board.display()
    
    if not scorce.end_game():
        if  millis() > startTime + DISPLAY_DURATION:
            if not gm.player_turn:
                display_massage = "player's turn..."
                ai.bestchoice()
                gm.player_turn = True
        fill(1)
        textSize(30)
        if display_massage == "player's turn...":
            t = "player's turn..."
            text(t, 310,400)
        elif display_massage == "computer's turn...":
            t = "computer's turn..."
            text(t, 290,400)
    else:
        scorce.draw_score_board()
        scorce.record_score()
            
def mousePressed():
    global startTime, display_massage
    if gm.player_turn:
        if not player.end_move():
            if player.do_move():
                display_massage = "computer's turn..."
                player.make_move()
                gm.player_turn = False
                startTime = millis()
            else:
                gm.player_turn = True
                display_massage = "player's turn..."
        else:
            gm.player_turn = False
            display_massage = "computer's turn.."
            startTime = millis()
        
