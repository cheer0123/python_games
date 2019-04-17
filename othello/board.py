from move import Move


class Board:
    """Draws the board and handles movements of two players"""

    def __init__(self):
        self.n = 8
        self.array = []
        for x in range(self.n):
            self.array.append([])
            for y in range(self.n):
                self.array[x].append(None)

        # Initializing center values
        self.array[self.n//2 - 1][self.n//2 - 1] = "w"
        self.array[self.n//2 - 1][self.n//2] = "b"
        self.array[self.n//2][self.n//2 - 1] = "b"
        self.array[self.n//2][self.n//2] = "w"
        self.oldarray = self.array

    def update(self):
        for x in range(self.n):
            for y in range(self.n):
                if self.oldarray[x][y] == "w":
                    fill(1)
                    ellipse(50+100*x, 50+100*y, 90, 90)
                elif self.oldarray[x][y] == "b":
                    fill(0)
                    ellipse(50+100*x, 50+100*y, 90, 90)

    def display(self):
        """Display the board"""
        self.update()
        stroke(0)
        strokeWeight(1)
        noFill()
        for i in range(0, self.n):
            for j in range(0, self.n):
                rect(100*i, 100*j, 100, 100)
