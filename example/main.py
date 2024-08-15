from maze_runner import Maze

if "__main__" == __name__:
    maze = Maze("../maps/03.txt")
    while not maze.has_finished():
        if maze.can_move_right():
            maze.move_right()
        else:
            maze.move_down()
        maze.print_maze_status()

    maze.generate_animation(
        # Add your own header message
        header="My amazing solution!\nBy https://github.com/YOUR_NICKNAME",
        # Higher fps means faster animation
        fps=2,
    )
