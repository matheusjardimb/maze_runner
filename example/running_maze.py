from maze_runner.maze import Maze

if "__main__" == __name__:
    maze = Maze("maps/04.csv")
    maze.clear_console()

    maze.print_maze_status()
    while not maze.has_finished():
        if maze.can_move_left():
            maze.move_left()
        else:
            maze.move_down()

    maze.print_maze_status()
    maze.generate_animation("My maze solution")
