import copy
import logging
import os
from time import sleep

from maze_runner.animation import create_gif
from maze_runner.position import Position

logger = logging.getLogger(__name__)


class Maze:
    EMPTY_CELL = 0
    WALL_MARKER = "#"
    START_POS_MARKER = "S"
    FINISH_POS_MARKER = "F"
    ACTUAL_POS_MARKER = "A"

    def __init__(
        self, maze_file_path: str, steps_limit: int = None, sleep_interval: float = 0.5
    ):
        super().__init__()

        if sleep_interval < 0:
            raise Exception("Sleep interval should be >= 0")
        self.__sleep_interval = sleep_interval

        self.__maze = []
        self.__positions = []
        self.__start_position = None
        self.__finish_positions = []

        maze_width = None

        # Start loading Maze file
        with open(maze_file_path) as file:
            lines = file.readlines()
            line_count = 0

            for y_pos, cells in enumerate(lines):
                cells = cells.replace("\n", "")
                # Validate maze width
                if maze_width is None:
                    maze_width = len(cells)
                elif maze_width != len(cells):
                    raise Exception("All lines should have the same width")

                # Validate has start position
                if self.START_POS_MARKER in cells:
                    x_pos = cells.index(self.START_POS_MARKER)
                    if x_pos != -1:
                        if self.__start_position is None:
                            self.__start_position = Position(x=x_pos, y=y_pos)
                            self.__positions.append(self.__start_position)
                        else:
                            raise Exception("Map should have ony one starting cell")

                row = []
                for x_pos, cell in enumerate(cells):
                    if cell == self.FINISH_POS_MARKER:
                        self.__finish_positions.append(Position(x=x_pos, y=y_pos))
                    row.append(1 if cell == self.WALL_MARKER else 0)
                self.__maze.append(row)
            print(f"Processed {line_count} lines.")

        if len(self.__finish_positions) == 0:
            raise Exception("Map has no finishing cells")
        else:
            logger.info(f"Found {len(self.__finish_positions)} finishing cell(s).")

        if steps_limit is None:
            maze_height = len(self.__maze)
            self.__step_limit = maze_width * maze_height * 4
        else:
            if steps_limit <= 1:
                raise Exception("Steps limit should be > 1")
            else:
                self.__step_limit = steps_limit

    def steps_taken_count(self):
        return len(self.__positions) - 1

    def get_maze_height(self):
        return len(self.__maze)

    def get_maze_width(self):
        return len(self.__maze[0])

    def get_steps_limit(self):
        return self.__step_limit

    def get_pending_steps(self):
        return self.get_steps_limit() - self.steps_taken_count()

    def generate_animation(self, header: str, fps: int = 1, filename: str = None):
        create_gif(
            header,
            self.__maze,
            self.__positions,
            self.__start_position,
            self.__finish_positions,
            fps,
            filename,
        )

    def print_maze_status(self, clean_console: bool = True) -> None:
        self.sleep(self.__sleep_interval)

        if clean_console:
            self.clear_console()

        print(f"Steps: {self.steps_taken_count()}/{self.get_steps_limit()}")
        maze = copy.deepcopy(self.__maze)
        maze = [
            [" " if cell == self.EMPTY_CELL else self.WALL_MARKER for cell in row]
            for row in maze
        ]
        maze[self.__start_position.y][self.__start_position.x] = self.START_POS_MARKER

        for finish_position in self.__finish_positions:
            maze[finish_position.y][finish_position.x] = self.FINISH_POS_MARKER

        cur_pos = self.get_current_position()
        maze[cur_pos.y][cur_pos.x] = self.ACTUAL_POS_MARKER

        lines = []
        for line in maze:
            print("".join(line))

        for line in lines:
            print(line)

        if self.has_finished():
            print(f"Exit found at {cur_pos} with {self.steps_taken_count()} steps.")

    def get_current_position(self):
        return self.__positions[-1]

    def has_finished(self) -> bool:
        return self.get_current_position() in self.__finish_positions

    @staticmethod
    def clear_console() -> None:
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def sleep(interval: float) -> None:
        sleep(interval)

    def can_move_to_position(self, new_pos: Position) -> bool:
        if new_pos.x < 0 or new_pos.y < 0:
            return False
        if (
            new_pos.x > self.get_maze_width() - 1
            or new_pos.y > self.get_maze_height() - 1
        ):
            return False
        return self.__maze[new_pos.y][new_pos.x] == self.EMPTY_CELL

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
        if self.steps_taken_count() > self.get_steps_limit():
            raise Exception("Step limit reached")

        new_pos = direction_method()
        if new_pos is not False:
            self.__positions.append(new_pos)
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
