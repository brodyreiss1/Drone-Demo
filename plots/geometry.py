import matplotlib.pyplot as plt
import os


def plot_geometry(array_coords, title="Array Geometry", save_path=None):
    x = array_coords[:, 0]
    y = array_coords[:, 1]

    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c='blue')
    plt.title(title)
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    plt.axis('equal')

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
