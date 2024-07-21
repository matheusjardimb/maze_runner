import csv
import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class Position:
    x: int
    y: int

    def new_position_up(self) -> "Position":
        return Position(self.x, self.y - 1)

    def new_position_down(self) -> "Position":
        return Position(self.x, self.y + 1)

    def new_position_left(self) -> "Position":
        return Position(self.x - 1, self.y)

    def new_position_right(self) -> "Position":
        return Position(self.x + 1, self.y)


class Maze:
    START_CELL = "S"
    FINISH_CELL = "F"

    maze: list = []
    finished: bool = False

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

                start_position = cells.index(self.START_CELL)
                if start_position != -1:
                    self.current_position = Position(idx, start_position)

                for cell_idx, cell in enumerate(cells):
                    if cell == self.FINISH_CELL:
                        self.finish_positions.append(Position(idx, cell_idx))

                start_cell_count += cells.count(self.START_CELL)
                finish_cell_count += cells.count(self.FINISH_CELL)
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
        for line in self.maze:
            print("".join(line))

    def has_finished(self) -> bool:
        return self.finished

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
        return self.maze[new_pos.y][new_pos.x].strip() == ""

    def can_move_up(self) -> bool:
        return self.can_move_to_position(self.current_position.new_position_up())

    def can_move_down(self) -> bool:
        return self.can_move_to_position(self.current_position.new_position_down())

    def can_move_left(self) -> bool:
        return self.can_move_to_position(self.current_position.new_position_left())

    def can_move_right(self) -> bool:
        return self.can_move_to_position(self.current_position.new_position_right())
