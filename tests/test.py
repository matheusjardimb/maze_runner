import unittest

from maze_runner.maze import Maze


class MultiStartPointException(Exception):
    pass


class MyTestCase(unittest.TestCase):
    def test1(self):
        def init_maze():
            Maze("csv/multi_start.csv")

        self.assertRaises(MultiStartPointException, init_maze)
