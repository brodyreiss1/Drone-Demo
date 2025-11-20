import numpy as np


def angles_to_target(tx_pos: np.ndarray, rx_pos: np.ndarray):
    rel = rx_pos - tx_pos
    x, y, z = rel

    az = np.arctan2(y, x)  # -pi..pi
    r_xy = np.sqrt(x * x + y * y)
    el = np.arctan2(z, r_xy)  # -pi/2..pi/2

    return az, el
