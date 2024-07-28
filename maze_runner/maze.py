import copy
import csv
import logging
import os
from time import sleep

from maze_runner.position import Position

logger = logging.getLogger(__name__)


class Maze:
    WALL_MARKER = "#"
    START_POS_MARKER = "S"
    FINISH_POS_MARKER = "F"
    ACTUAL_POS_MARKER = "A"

    def __init__(self, maze_file_path: str):
        super().__init__()
        self.maze = []

        self.maze_width = None
        self.maze_height = 0

        self.positions = []
        self.start_position = None
        self.finish_positions = []

        # Start loading Maze file
        with open(maze_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            row = []
            for y_pos, cells in enumerate(csv_reader):
                # Validate maze width
                if self.maze_width is None:
                    self.maze_width = len(cells)
                elif self.maze_width != len(cells):
                    raise Exception("All lines should have the same width")

                # Validate has start position
                x_pos = cells.index(self.START_POS_MARKER)
                if x_pos != -1:
                    if self.start_position is None:
                        self.start_position = Position(x=x_pos, y=y_pos)
                        self.positions.append(self.start_position)
                    else:
                        raise Exception("Map should have ony one starting cell")

                for x_pos, cell in enumerate(cells):
                    if cell == self.FINISH_POS_MARKER:
                        self.finish_positions.append(Position(x=x_pos, y=y_pos))

                    row.append(1 if cell == self.WALL_MARKER else 0)

                self.finish_positions.append(cells.count(self.FINISH_POS_MARKER))
                self.maze.append(cells)
            print(f"Processed {line_count} lines.")

        self.maze_height = len(self.maze)

        if len(self.finish_positions) == 0:
            raise Exception("Map has no finishing cells")
        else:
            logger.info(f"Found {len(self.finish_positions)} finishing cell(s).")

        self.step_limit = self.maze_width * self.maze_height
        self.steps_taken = 0

    def print_maze_status(
        self, clean_console: bool = True, sleep_after_print: float = 0.5
    ) -> None:
        self.sleep(sleep_after_print)

        if clean_console:
            self.clear_console()

        print(f"Steps: {self.steps_taken}/{self.step_limit}")
        maze = copy.deepcopy(self.maze)
        cur_pos = self.get_current_position()
        maze[cur_pos.y][cur_pos.x] = self.ACTUAL_POS_MARKER
        lines = []
        for line in maze:
            print("".join(line))

        for line in lines:
            print(line)

        if self.has_finished():
            print(f"Exit found at {cur_pos} with {self.steps_taken} steps.")

    def get_current_position(self):
        return self.positions[-1]

    def has_finished(self) -> bool:
        return self.get_current_position() in self.finish_positions

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

    def __can_move_to(self, new_pos) -> Position | bool:
        if self.can_move_to_position(new_pos):
            return new_pos
        return False

    def can_move_up(self) -> Position | bool:
        return self.__can_move_to(self.get_current_position().new_position_up())

    def can_move_down(self) -> Position | bool:
        return self.__can_move_to(self.get_current_position().new_position_down())

    def can_move_left(self) -> Position | bool:
        return self.__can_move_to(self.get_current_position().new_position_left())

    def can_move_right(self) -> Position | bool:
        return self.__can_move_to(self.get_current_position().new_position_right())

    def __move_position(self, direction_method) -> bool:
        self.print_maze_status()
        if self.steps_taken > self.step_limit:
            raise Exception("Step limit reached")
        self.steps_taken += 1

        new_pos = direction_method()
        if new_pos is not False:
            self.positions.append(new_pos)
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
