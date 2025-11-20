import numpy as np


def ura(Nx, Ny, dx, dy):
    x = np.arange(Nx) * dx - (Nx - 1) * dx / 2
    y = np.arange(Ny) * dy - (Ny - 1) * dy / 2
    X, Y = np.meshgrid(x, y)
    return np.vstack((X.flatten(), Y.flatten(), np.zeros(X.size))).T
