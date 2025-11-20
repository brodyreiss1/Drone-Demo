import numpy as np


def array_gain(AF):
    return np.abs(AF)**2


def array_gain_db(AF):
    # Had issues with log of zero, so I added a very small consntant
    return 20 * np.log10(np.abs(AF) + 1e-12)
