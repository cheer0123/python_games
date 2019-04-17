from pacman import Pacman
from maze import Maze
from game_controller import GameController


def test_constructor():
    game_controller = GameController(600, 400)
    maze = Maze(600, 400, 150, 450,
                100, 300, game_controller)
    pacman = Pacman(maze, game_controller)
    assert pacman.gc is game_controller
    assert pacman.maze is maze


def test_eat_dots():
    game_controller = GameController(600, 600)
    maze = Maze(600, 600, 150, 450,
                150, 450, game_controller)
    pacman = Pacman(maze, game_controller)

    pacman.y = 150
    pacman.x = 0
    assert len(pacman.maze.dots.top_row) == 9
    pacman.eat_dots()
    assert len(pacman.maze.dots.top_row) == 8

    pacman.y = 450
    pacman.x = 150
    assert len(pacman.maze.dots.bottom_row) == 9
    assert len(pacman.maze.dots.left_col) == 9
    pacman.eat_dots()
    assert len(pacman.maze.dots.bottom_row) == 8
    assert len(pacman.maze.dots.left_col) == 8

    pacman.y = 450
    pacman.x = 450
    assert len(pacman.maze.dots.bottom_row) == 8
    assert len(pacman.maze.dots.right_col) == 9
    pacman.eat_dots()
    assert len(pacman.maze.dots.bottom_row) == 7
    assert len(pacman.maze.dots.right_col) == 8

    pacman.y = 150
    pacman.x = 600
    assert len(pacman.maze.dots.top_row) == 8
    pacman.eat_dots()
    assert len(pacman.maze.dots.top_row) == 7
