import numpy as np

from .array_factor import array_factor


def sweep_azimuth(coords, elevation=0.0, num_points=360):
    phis = np.linspace(0, 2 * np.pi, num_points)
    af_values = np.array([
        abs(array_factor(coords, elevation, phi))
        for phi in phis
    ])
    return phis, af_values


def sweep_2d(coords, num_az=360, num_el=181):
    phis = np.linspace(0, 2 * np.pi, num_az)              # azimuth
    elevations = np.linspace(-np.pi/2, np.pi/2, num_el)   # elevation

    AF = np.zeros((num_el, num_az))

    for i, el in enumerate(elevations):
        for j, phi in enumerate(phis):
            AF[i, j] = abs(array_factor(coords, el, phi))

    return elevations, phis, AF
