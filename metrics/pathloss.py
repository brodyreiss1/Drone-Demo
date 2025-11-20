import numpy as np


def fspl(distance, wavelength):
    return (4 * np.pi * distance / wavelength) ** 2


def fspl_db(distance, wavelength):
    return 20 * np.log10(4 * np.pi * distance / wavelength)
