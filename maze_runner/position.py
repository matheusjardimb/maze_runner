import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class Position:
    x: int
    y: int

    def __str__(self):
        return f"X={self.x}, Y={self.y}"

    def to_tuple_yx(self) -> tuple:
        return self.y, self.x

    def new_position_up(self) -> "Position":
        return Position(self.x, self.y - 1)

    def new_position_down(self) -> "Position":
        return Position(self.x, self.y + 1)

    def new_position_left(self) -> "Position":
        return Position(self.x - 1, self.y)

    def new_position_right(self) -> "Position":
        return Position(self.x + 1, self.y)
