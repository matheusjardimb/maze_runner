import os
import glob

from ..maze import Maze


def test_validate_sample_maps():
    folder_path = "../maps"
    txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
    for file in txt_files:
        Maze(file)  # Simply instantiate a maze using each map
