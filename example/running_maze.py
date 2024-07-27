from maze_runner.maze import Maze

if "__main__" == __name__:
    maze = Maze("maze_runner/maps/02.csv")
    maze.clear_console()

    maze.print_maze_status()
    while not maze.has_finished():
        if maze.can_move_left():
            maze.move_left()

    maze.print_maze_status()
    print(f"Exit found at {maze.current_position}")
