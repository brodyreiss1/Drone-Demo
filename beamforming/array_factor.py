import numpy as np

from constants.params import WAVELENGTH


def array_factor(coords, elevation, azimuth):
    kx = np.cos(elevation) * np.cos(azimuth)
    ky = np.cos(elevation) * np.sin(azimuth)
    kz = np.sin(elevation)

    # Wave vector
    k = (2 * np.pi / WAVELENGTH)
    k_vec = k * np.array([kx, ky, kz])

    # Phase for each element
    phase = coords @ k_vec

    AF = np.sum(np.exp(1j * phase))

    AF /= len(coords)

    return AF
