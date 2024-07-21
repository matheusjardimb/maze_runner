import copy
import csv
import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class Position:
    x: int
    y: int

    def __str__(self):
        return f"X={self.x}, Y={self.y}"

    def new_position_up(self) -> "Position":
        return Position(self.x, self.y - 1)

    def new_position_down(self) -> "Position":
        return Position(self.x, self.y + 1)

    def new_position_left(self) -> "Position":
        return Position(self.x - 1, self.y)

    def new_position_right(self) -> "Position":
        return Position(self.x + 1, self.y)


class Maze:
    START_POS_MARKER = "S"
    FINISH_POS_MARKER = "F"
    ACTUAL_POS_MARKER = "A"

    maze: list = []

    maze_width: int = None
    maze_height: int = 0

    current_position: Position
    start_position: Position
    finish_positions: list[Position] = []

    def __init__(self, maze_file_path: str):
        super().__init__()
        self.load_maze_file(maze_file_path)

    def load_maze_file(self, maze_file_path):
        start_cell_count = 0
        finish_cell_count = 0
        with open(maze_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            for idx, cells in enumerate(csv_reader):
                if self.maze_width is None:
                    self.maze_width = len(cells)
                elif self.maze_width != len(cells):
                    raise Exception("All lines should have the same width")

                start_position = cells.index(self.START_POS_MARKER)
                if start_position != -1:
                    self.current_position = Position(idx, start_position)

                for cell_idx, cell in enumerate(cells):
                    if cell == self.FINISH_POS_MARKER:
                        self.finish_positions.append(Position(x=cell_idx, y=idx))

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

    def print_maze_status(self) -> None:
        maze = copy.deepcopy(self.maze)
        maze[self.current_position.y][self.current_position.x] = self.ACTUAL_POS_MARKER
        for line in maze:
            print("".join(line))

    def has_finished(self) -> bool:
        return self.current_position in self.finish_positions

    @staticmethod
    def clear_console() -> None:
        import os

        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def sleep(interval: float = 0.5) -> None:
        import time

        time.sleep(interval)

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

    def move_up(self) -> bool:
        new_pos = self.can_move_up()
        if not new_pos:
            self.current_position = new_pos
            return True
        return False

    def move_down(self) -> bool:
        new_pos = self.can_move_down()
        if not new_pos:
            self.current_position = new_pos
            return True
        return False

    def move_left(self) -> bool:
        new_pos = self.can_move_left()
        if not new_pos:
            self.current_position = new_pos
            return True
        return False

    def move_right(self) -> bool:
        new_pos = self.can_move_right()
        if new_pos:
            self.current_position = new_pos
            return True
        return False
