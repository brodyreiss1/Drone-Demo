import numpy as np

C = 3e8  # Speed of light in m/s
FREQ = 6e9  # 6 GHz
WAVELENGTH = C / FREQ  # Wavelength
D = WAVELENGTH / 2  # Element spacing
UCA_DEFAULT_RADIUS = 1.5 * D

K = 1.38064852e-23  # Boltzmann constant in J/K
T = 290  # Standard temperature in Kelvin