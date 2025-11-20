import numpy as np

from constants.params import K, T


def noise_power(bandwidth, noise_figure_db=5):
    N = K * T * bandwidth
    NF = 10 ** (noise_figure_db / 10)
    return N * NF


def snr(received_power, noise):
    return received_power / noise
