import datetime

import imageio
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np


# Function to plot the maze and the current position
def plot_maze(
    maze,
    position=None,
    path=None,
    text_above=None,
    text_below=None,
    green_cells=None,
    yellow_cells=None,
):
    fig, ax = plt.subplots(figsize=(5, 7))  # Increase figure height for text
    ax.imshow(maze, cmap="binary")

    if green_cells:
        for cell in green_cells:
            rect = patches.Rectangle(
                (cell[1] - 0.5, cell[0] - 0.5),
                1,
                1,
                linewidth=1,
                edgecolor="none",
                facecolor="green",
                alpha=0.3,
            )
            ax.add_patch(rect)

    if yellow_cells:
        for cell in yellow_cells:
            rect = patches.Rectangle(
                (cell[1] - 0.5, cell[0] - 0.5),
                1,
                1,
                linewidth=1,
                edgecolor="none",
                facecolor="yellow",
                alpha=0.3,
            )
            ax.add_patch(rect)

    if path:
        for p in path:
            ax.plot(p[1], p[0], "bo")  # Path points in blue

    if position:
        ax.plot(position[1], position[0], "ro")  # Current position in red

    ax.axis("off")

    if text_above:
        fig.text(
            0.5,
            0.95,
            text_above,
            fontsize=12,
            color="black",
            ha="center",
            va="center",
            bbox=dict(facecolor="white", alpha=0.5),
        )

    if text_below:
        fig.text(
            0.5,
            0.05,
            text_below,
            fontsize=12,
            color="black",
            ha="center",
            va="center",
            bbox=dict(facecolor="white", alpha=0.5),
        )

    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype="uint8")
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)
    return image


def create_gif(header, maze, path, start_position, finish_positions):
    # Create a simple maze (0: path, 1: wall)
    maze = np.array(maze)

    # Define the path (sequence of (row, col) positions)
    path = [(cell.y, cell.x) for cell in path]

    # Define green and yellow cells
    green_cells = [(start_position.y, start_position.x)]
    yellow_cells = [(cell.y, cell.x) for cell in finish_positions]

    # Create frames for each step in the path
    frames = []
    for i, pos in enumerate(path):
        image = plot_maze(
            maze,
            position=pos,
            path=path[: i + 1],
            text_above=header,
            text_below="matheusjardimb.com",
            green_cells=green_cells,
            yellow_cells=yellow_cells,
        )
        frames.append(image)

    # Save frames as a GIF
    imageio.mimsave(
        f"maze_path_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.gif",
        frames,
        fps=1,
    )
