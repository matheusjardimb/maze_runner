from maze import Maze

if "__main__" == __name__:
    maze = Maze("maps/02.csv")
    maze.clear_console()

    while not maze.has_finished():
        maze.print_maze_status()

        if maze.can_move_left():
            maze.move_left()

    maze.print_maze_status()
    print(f"Exit found at {maze.current_position}")
