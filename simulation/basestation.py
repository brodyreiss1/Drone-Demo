import numpy as np


class BaseStation:
    def __init__(self, position, array_coords):
        self.position = np.array(position, dtype=float)
        self.array_coords = array_coords
