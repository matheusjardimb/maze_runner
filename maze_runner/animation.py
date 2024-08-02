import datetime

import imageio
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np


def draw_cells(ax, cells, color):
    if cells:
        for cell in cells:
            rect = patches.Rectangle(
                (cell[1] - 0.5, cell[0] - 0.5),
                1,
                1,
                linewidth=1,
                edgecolor="none",
                facecolor=color,
                alpha=0.3,
            )
            ax.add_patch(rect)


def plot_maze(
    maze,
    position=None,
    path=None,
    text_above=None,
    text_below=None,
    green_cells=None,
    yellow_cells=None,
):
    fig, ax = plt.subplots(figsize=(5, 6))  # Increase figure height for text
    ax.imshow(maze, cmap="binary")

    draw_cells(ax, green_cells, "green")
    draw_cells(ax, yellow_cells, "yellow")

    if path:
        for p in path:
            draw_cells(ax, yellow_cells, "yellow")
            rect = patches.Rectangle(
                (p[1] - 0.5, p[0] - 0.5),
                1,
                1,
                linewidth=1,
                edgecolor="none",
                facecolor="red",
                alpha=0.1,
            )
            ax.add_patch(rect)
            ax.plot(p[1], p[0], "bo")  # Path points in blue

    if position:
        ax.plot(position[1], position[0], "ro")  # Current position in red

    ax.axis("off")

    if text_above:
        fig.text(
            0.5,
            0.9,
            text_above,
            alpha=1,
            fontsize=12,
            color="black",
            ha="center",
            va="center",
            bbox=dict(facecolor="none", alpha=0.0),
        )

    if text_below:
        fig.text(
            0.5,
            0.1,
            text_below,
            alpha=0.5,
            fontsize=12,
            color="black",
            ha="center",
            va="center",
            bbox=dict(facecolor="none", alpha=0.0),
        )

    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype="uint8")
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)
    return image


def create_gif(
    header,
    maze,
    path,
    start_position,
    finish_positions,
    fps: int = 1,
    filename: str = None,
):
    if fps < 1:
        raise Exception("fps must be >= 1")

    maze = np.array(maze)

    # Define the path (sequence of (row, col) positions)
    path = [(cell.y, cell.x) for cell in path]

    # Define green and yellow cells
    green_cells = [start_position.to_tuple_yx()]
    yellow_cells = [cell.to_tuple_yx() for cell in finish_positions]

    # Create frames for each step in the path
    frames = []
    for i, pos in enumerate(path):
        image = plot_maze(
            maze,
            position=pos,
            path=path[: i + 1],
            text_above=header,
            # Please, keep the reference to the source repo. Feel free to fork it and contribute!
            text_below="https://github.com/matheusjardimb/maze_runner",
            green_cells=green_cells,
            yellow_cells=yellow_cells,
        )
        frames.append(image)

    if not filename:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"maze_path_{timestamp}.gif"

    # Save frames as a GIF
    imageio.mimsave(filename, frames, fps=fps)
