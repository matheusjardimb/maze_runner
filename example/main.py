from maze_runner import Maze

if "__main__" == __name__:
    maze = Maze("../maps/02.txt")
    maze.clear_console()

    maze.print_maze_status()

    while not maze.has_finished():
        if maze.can_move_left():
            maze.move_left()
        else:
            maze.move_down()

    maze.print_maze_status()
    # Add your own GitHub Page
    maze.generate_animation(
        header="My amazing maze solution!\nBy: https://github.com/matheusjardimb", fps=2
    )
