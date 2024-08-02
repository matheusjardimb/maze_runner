import random


class MazeGenerator:
    # Movimentos possíveis
    MOVES = [(0, 2), (2, 0), (0, -2), (-2, 0)]

    @staticmethod
    def generate_maze_structure(width: int = 21, height: int = 21):
        # Inicializa o labirinto com paredes
        maze = [["#" for _ in range(width)] for _ in range(height)]

        # Função recursiva para criar o labirinto
        def carve_passages_from(x, y):
            directions = MazeGenerator.MOVES[:]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == "#":
                    if 1 <= nx < width - 1 and 1 <= ny < height - 1:
                        maze[ny][nx] = " "
                        maze[ny - dy // 2][nx - dx // 2] = " "
                        carve_passages_from(nx, ny)

        # Define o ponto de partida
        start_x, start_y = (1, 1)
        maze[start_y][start_x] = "S"
        carve_passages_from(start_x, start_y)

        # TODO add multi exits
        # exits = [(width - 2, height - 2)]
        maze[height - 2][width - 2] = "F"

        return maze

    @staticmethod
    def save_maze_to_file(maze, filename):
        with open(filename, "w", newline="") as file:
            file.writelines([f"{''.join(line)}\n" for line in maze])
