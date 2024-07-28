import datetime
import numpy as np
import matplotlib.pyplot as plt
import imageio
import matplotlib.patches as patches


# Function to plot the maze and the current position
def plot_maze(
    maze, position=None, path=None, text=None, green_cells=None, yellow_cells=None
):
    fig, ax = plt.subplots(figsize=(5, 6))  # Increase figure height for text
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

    if text:
        fig.text(
            0.5,
            0.05,
            text,
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


def create_gif():
    # Create a simple maze (0: path, 1: wall)
    maze = np.array(
        [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]
    )

    # Define the path (sequence of (row, col) positions)
    path = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5)]

    # Define green and yellow cells
    green_cells = [(1, 1), (2, 3)]
    yellow_cells = [(1, 2), (3, 4)]

    # Create frames for each step in the path
    frames = []
    for i, pos in enumerate(path):
        image = plot_maze(
            maze,
            position=pos,
            path=path[: i + 1],
            text="matheusjardimb.com",
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


create_gif()
