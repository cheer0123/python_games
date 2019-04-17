

class Move:
    def __init__(self, board):
        self.board = board
        self.valid_moves = []

    def is_on_board(self, x, y):
        # Returns True if the coordinates are located on the board.
        if x >= 0 and x <= 7 and y >= 0 and y <= 7:
            return True
        else:
            return False

    def valid_move(self, x, y):
        if self.is_on_board(x, y):
            if self.board.array[x][y] != "w" and self.board.array[x][y] != "b":
                return True
        return False

    def tiles_to_flip(self, x, y, tile):
        self.to_flip = []
        if tile == 'w':
            othertile = 'b'
        else:
            othertile = 'w'
        directions = [[0, 1], [1, 1], [1, 0], [1, -1],
                      [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        xstart = x
        ystart = y
        for xdirection, ydirection in directions:
            x = xstart
            y = ystart
            x += xdirection
            y += ydirection
            if self.is_on_board(x, y) and self.board.array[x][y] == othertile:
                # There is a piece belonging to the other player next to our piece.
                x += xdirection
                y += ydirection
                if not self.is_on_board(x, y):
                    continue
                while self.board.array[x][y] == othertile:
                    x += xdirection
                    y += ydirection
                    # break out of while loop, then continue in for loop
                    if not self.is_on_board(x, y):
                        break
                if not self.is_on_board(x, y):
                    continue
                if self.board.array[x][y] == tile:
                    # There are pieces to flip over. Go in the reverse direction until we
                    # reach the original space, noting all the tiles along the way.
                    while True:
                        x -= xdirection
                        y -= ydirection
                        if x == xstart and y == ystart:
                            break
                        self.to_flip.append([x, y])
            else:
                continue
        if len(self.to_flip) == 0:
            return False
        else:
            return self.to_flip

    def make_move(self, x, y, tile):
        # Place the tile on the board at xstart, ystart, and flip any of the opponent's pieces.
        if self.valid_move(x, y) and self.tiles_to_flip(x, y, tile):
            if tile == 'b':
                self.board.array[x][y] = "b"
            elif tile == 'w':
                self.board.array[x][y] = "w"
            tiles_to_flip = self.tiles_to_flip(x, y, tile)
            for i, j in tiles_to_flip:
                self.board.array[i][j] = tile

    def get_valid_moves(self, tile):
        valid_moves = []
        for x in range(8):
            for y in range(8):
                if self.valid_move(x, y) != False:
                    if self.tiles_to_flip(x, y, tile):
                        valid_moves.append([x, y])
        if len(valid_moves) == 0:
            return False
        else:
            return valid_moves
