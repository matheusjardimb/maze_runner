import csv
from collections import deque


def load_maze_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        maze = [list(row) for row in reader]
    return maze


def find_start_and_exits(maze):
    start = None
    exits = []
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'F':
                exits.append((x, y))
    return start, exits


def bfs(maze, start, exits):
    width = len(maze[0])
    height = len(maze)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in exits:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None


def print_maze_with_path(maze, path):
    maze_with_path = [row[:] for row in maze]
    for (x, y) in path:
        if maze_with_path[y][x] == ' ':
            maze_with_path[y][x] = '.'

    for row in maze_with_path:
        print(''.join(row))


if __name__ == "__main__":
    filename = '../maps/10.csv'
    maze = load_maze_from_csv(filename)
    start, exits = find_start_and_exits(maze)

    if start is None or not exits:
        print("O labirinto não tem ponto de partida ou saídas.")
    else:
        path = bfs(maze, start, exits)
        if path:
            print("Caminho encontrado:")
            print_maze_with_path(maze, path)
        else:
            print("Nenhum caminho encontrado.")
