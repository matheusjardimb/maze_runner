from maze import Maze

if "__main__" == __name__:
    maze = Maze("maps/01.csv")
    while not maze.has_finished():
        available_movements = ["can_move_up"] if maze.can_move_up() else []
        available_movements.append("can_move_down") if maze.can_move_down() else None
        available_movements.append("can_move_left") if maze.can_move_left() else None
        available_movements.append("can_move_right") if maze.can_move_right() else None
        print(", ".join(available_movements))

        maze.print_maze_status()
        maze.sleep()
        maze.clear_console()
