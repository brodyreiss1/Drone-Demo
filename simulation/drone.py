import numpy as np


class Drone:
    def __init__(self, path_fn, tx_power_dbm: float = 20.0):
        self.path_fn = path_fn
        self.tx_power_dbm = tx_power_dbm
        self.position = np.zeros(3, dtype=float)

    def update(self, t: float):
        self.position = np.asarray(self.path_fn(t), dtype=float)
