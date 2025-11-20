import numpy as np


class Environment:
    def __init__(self, dt: float = 0.1, duration: float = 10.0):
        self.dt = dt
        self.duration = duration

    def time_grid(self) -> np.ndarray:
        n_steps = int(self.duration / self.dt) + 1
        return np.linspace(0.0, self.duration, n_steps)
