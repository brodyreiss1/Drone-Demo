import numpy as np

from constants.params import WAVELENGTH, K, T
from beamforming.array_factor import array_factor
from .geometry import angles_to_target

from metrics.pathloss import fspl_db
from metrics.snr import snr


class Channel:
    def __init__(self, bandwidth_hz: float = 20e6, noise_figure_db: float = 5.0):
        self.bandwidth_hz = bandwidth_hz
        self.noise_figure_db = noise_figure_db

    @staticmethod
    def db_to_linear(db):
        return 10.0 ** (db / 10.0)

    @staticmethod
    def linear_to_db(x):
        return 10.0 * np.log10(x)

    def noise_power_w(self):
        nf_lin = self.db_to_linear(self.noise_figure_db)
        return K * T * self.bandwidth_hz * nf_lin

    def compute_link(self, drone, basestation):
        # Distance
        d_vec = drone.position - basestation.position
        distance_m = float(np.linalg.norm(d_vec))

        # Angles from BS → drone
        az, el = angles_to_target(basestation.position, drone.position)

        # Array factor
        af = array_factor(basestation.array_coords, el, az)

        # POWER GAIN = |AF|²  (linear)
        array_gain_linear = np.abs(af) ** 2
        array_gain_db = 10 * np.log10(array_gain_linear + 1e-30)

        # Path loss in dB (uses metrics.pathloss.fspl_db)
        pathloss_db = fspl_db(distance_m, WAVELENGTH)

        # Receiver power
        tx_power_dbm = drone.tx_power_dbm
        rx_power_dbm = tx_power_dbm + array_gain_db - pathloss_db

        # Convert to Watts
        rx_power_w = 1e-3 * self.db_to_linear(rx_power_dbm)

        # Noise power
        noise_w = self.noise_power_w()

        # SNR (uses metrics.snr)
        snr_linear = snr(rx_power_w, noise_w)
        snr_db = self.linear_to_db(snr_linear + 1e-30)

        # Capacity
        capacity_bps = self.bandwidth_hz * np.log2(1 + snr_linear)

        return {
            "distance_m": distance_m,
            "azimuth_rad": az,
            "elevation_rad": el,
            "array_factor": af,
            "array_gain_db": array_gain_db,
            "pathloss_db": pathloss_db,
            "rx_power_dbm": rx_power_dbm,
            "snr_linear": snr_linear,
            "snr_db": snr_db,
            "capacity_bps": capacity_bps,
        }
