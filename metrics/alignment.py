import numpy as np


def pointing_error(theta_target, theta_actual):
    return np.abs(theta_target - theta_actual)
