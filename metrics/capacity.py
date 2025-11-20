import numpy as np


def shannon_capacity(bandwidth, snr_linear):
    return bandwidth * np.log2(1 + snr_linear)
