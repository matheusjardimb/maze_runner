from maze_runner.maze_creator import MazeGenerator

maze = MazeGenerator.generate_maze_structure()
MazeGenerator.save_maze_to_file(maze, "labirinto.txt")
