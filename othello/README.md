# othello
## A simple game of othello with an AI opponent.

###Description
Othello is a game that is played in a player vs. computer format. 
The game takes place on an 8x8 grid filled with pieces of alternating colour. The players take turns placing tiles of their respective colours. If placing the tile creates a continuous line of tiles with their colour at the beginning and end of the line, all the tiles in the line “flip” to become their colour.

For a move to be valid it must create one of the aforementioned lines. If there are no valid moves, you must pass your turn to your opponent.
The game is completed once both players cannot move, and the player with more tiles of their colour on the board wins.

###Instructions to Play
To play Othello, install processing first, the run the file othell_game.pyde in Processing. 

When it is your turn, you'll see green dots showing all of your valid moves. Clicking one of these dots will make a move and it will now be the computer's turn.

If you wish to restart or create a new game, you may press the "Restart" button in the top left of the screen. To quit, you may press the "Quit" button in the top right of the screen.

###TO DO:
- Improve AI algorithm to dynamic weight strategy

###DONE:
- Player turn indicator
- Restart/Quit GUI
- Animation for changing tiles
- output file for game records
