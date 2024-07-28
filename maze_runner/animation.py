import numpy as np
import matplotlib.pyplot as plt
import imageio


# Function to plot the maze and the current position
def plot_maze(maze, position=None, path=None, text=None):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(maze, cmap="binary")

    if path:
        for p in path:
            ax.plot(p[1], p[0], "bo")  # Path points in blue

    if position:
        ax.plot(position[1], position[0], "ro")  # Current position in red

    if text:
        # Add text to the bottom right corner
        # Adjust the coordinates to fit your needs
        plt.text(
            maze.shape[1] - 1,
            maze.shape[0] - 1,
            text,
            fontsize=12,
            color="black",
            ha="right",
            va="bottom",
            bbox=dict(facecolor="white", alpha=0.5),
        )

    ax.axis("off")
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

    # Create frames for each step in the path
    frames = []
    for i, pos in enumerate(path):
        image = plot_maze(
            maze, position=pos, path=path[: i + 1], text="matheusjardimb.com"
        )
        frames.append(image)

    # Save frames as a GIF
    imageio.mimsave("maze_path.gif", frames, fps=1)


create_gif()
