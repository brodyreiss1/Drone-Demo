import numpy as np


def ula(N, d):
    n = np.arange(N)
    x = (n - (N - 1) / 2) * d
    return np.vstack((x, np.zeros(N), np.zeros(N))).T
