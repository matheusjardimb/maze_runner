import copy
import csv
import logging
import os
from time import sleep

from maze_runner.position import Position

logger = logging.getLogger(__name__)


class Maze:
    START_POS_MARKER = "S"
    FINISH_POS_MARKER = "F"
    ACTUAL_POS_MARKER = "A"

    def __init__(self, maze_file_path: str):
        super().__init__()
        self.maze = []

        self.maze_width = None
        self.maze_height = 0

        self.current_position = None
        self.start_position = None
        self.finish_positions = []

        # Start loading Maze file
        start_cell_count = 0
        finish_cell_count = 0
        with open(maze_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            for y_pos, cells in enumerate(csv_reader):
                # Validate maze width
                if self.maze_width is None:
                    self.maze_width = len(cells)
                elif self.maze_width != len(cells):
                    raise Exception("All lines should have the same width")

                # Validate has start position
                x_pos = cells.index(self.START_POS_MARKER)
                if x_pos != -1:
                    self.current_position = Position(x=x_pos, y=y_pos)

                for x_pos, cell in enumerate(cells):
                    if cell == self.FINISH_POS_MARKER:
                        self.finish_positions.append(Position(x=x_pos, y=y_pos))

                start_cell_count += cells.count(self.START_POS_MARKER)
                finish_cell_count += cells.count(self.FINISH_POS_MARKER)
                self.maze.append(cells)
            print(f"Processed {line_count} lines.")

        self.maze_height = len(self.maze)
        if start_cell_count != 1:
            raise Exception("Map should have one starting cell")
        if finish_cell_count < 1:
            raise Exception("Map has no finishing cells")
        else:
            logger.info(f"Found {finish_cell_count} finishing cells.")

        self.step_limit = self.maze_width * self.maze_height

    def print_maze_status(
        self, clean_console: bool = True, sleep_after_print: float = 0.5
    ) -> None:
        self.sleep(sleep_after_print)

        if clean_console:
            self.clear_console()

        maze = copy.deepcopy(self.maze)
        maze[self.current_position.y][self.current_position.x] = self.ACTUAL_POS_MARKER
        lines = []
        for line in maze:
            print("".join(line))

        for line in lines:
            print(line)

    def has_finished(self) -> bool:
        return self.current_position in self.finish_positions

    @staticmethod
    def clear_console() -> None:
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def sleep(interval: float) -> None:
        sleep(interval)

    def can_move_to_position(self, new_pos: Position) -> bool:
        if new_pos.x < 0 or new_pos.y < 0:
            return False
        if new_pos.x > self.maze_width - 1 or new_pos.y > self.maze_height - 1:
            return False
        cell_data = self.maze[new_pos.y][new_pos.x].strip()
        return (
            cell_data == ""
            or cell_data == self.FINISH_POS_MARKER
            or cell_data == self.START_POS_MARKER
        )

    def can_move_up(self) -> Position | bool:
        new_pos = self.current_position.new_position_up()
        if self.can_move_to_position(new_pos):
            return new_pos
        return False

    def can_move_down(self) -> Position | bool:
        new_pos = self.current_position.new_position_down()
        if self.can_move_to_position(new_pos):
            return new_pos
        return False

    def can_move_left(self) -> Position | bool:
        new_pos = self.current_position.new_position_left()
        if self.can_move_to_position(new_pos):
            return new_pos
        return False

    def can_move_right(self) -> Position | bool:
        new_pos = self.current_position.new_position_right()
        if self.can_move_to_position(new_pos):
            return new_pos
        return False

    def __move_position(self, direction_method) -> bool:
        self.print_maze_status()
        if self.step_limit == 0:
            raise Exception("Step limit reached")
        self.step_limit -= 1

        new_pos = direction_method()
        if new_pos is not False:
            self.current_position = new_pos
            return True
        print("Step missed, can't move in this direction")
        return False

    def move_up(self) -> bool:
        return self.__move_position(self.can_move_up)

    def move_down(self) -> bool:
        return self.__move_position(self.can_move_down)

    def move_left(self) -> bool:
        return self.__move_position(self.can_move_left)

    def move_right(self) -> bool:
        return self.__move_position(self.can_move_right)
