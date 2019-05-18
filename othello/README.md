# othello
## A simple game of othello with an AI opponent.

###Description
Othello is a game that is played in a player vs. computer format. 
The game takes place on an 8x8 grid filled with pieces of alternating colour. The players take turns placing tiles of their respective colours. If placing the tile creates a continuous line of tiles with their colour at the beginning and end of the line, all the tiles in the line “flip” to become their colour.

For a move to be valid it must create one of the aforementioned lines. If there are no valid moves, you must pass your turn to your opponent.
The game is completed once both players cannot move, and the player with more tiles of their colour on the board wins.

###Instructions to Play
To play Othello, install processing first, the run the file othell_game.pyde in Processing. 

# My Heuristic
My evaluation function is that assigns a weighted value to each square on the 8x8 board (got weighted values from source).

The corner squares are worth the most (120) because they are the most important squares in the game. They cannot be flipped once placed. If you own two adjacent corners, you probably will own the connecting side.

The squares immediately adjacent (including diagonally) to the corner squares are worth a lot of negative points (-20, -40) because they help your opponent take the corner squares.
The squares two spaces away from the corners are worth a good amount of points (20, 15) because they help you obtain the corner squares.

For the rest of the board, generally, squares close to the center are worth a few points and those a little farther away are worth a few negative points. This is based off basic Othello strategy.

Using minimax algorithm with limiting depth to make the AI player smarter

###TO DO:
- Improve AI algorithm with Alpha-beta pruning

###DONE:
- Player turn indicator
- Restart/Quit GUI
- Animation for changing tiles
- output file for game records
