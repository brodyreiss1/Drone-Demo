import numpy as np


def uca(N, r):
    angles = np.linspace(0, 2*np.pi, N, endpoint=False)
    x = r * np.cos(angles)
    y = r * np.sin(angles)
    return np.vstack((x, y, np.zeros(N))).T
