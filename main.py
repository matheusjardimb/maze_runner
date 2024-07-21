from maze import Maze

if "__main__" == __name__:
    maze = Maze("maps/01.csv")
    maze.clear_console()

    while not maze.has_finished():
        maze.print_maze_status()
        maze.sleep()
        maze.clear_console()

        if maze.can_move_right():
            maze.move_right()

    maze.print_maze_status()
    print(f"Exit found at {maze.current_position}")
