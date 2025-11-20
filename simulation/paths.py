import numpy as np


def straight_path(start, direction, speed):
    start = np.array(start, dtype=float)
    direction = np.array(direction, dtype=float)
    direction = direction / np.linalg.norm(direction)

    def path(t: float) -> np.ndarray:
        return start + direction * speed * t

    return path


def circular_path(center, radius: float, altitude: float, angular_speed: float):
    cx, cy = center

    def path(t: float) -> np.ndarray:
        x = cx + radius * np.cos(angular_speed * t)
        y = cy + radius * np.sin(angular_speed * t)
        z = altitude
        return np.array([x, y, z], dtype=float)

    return path
