import numpy as np


class Simulator:
    def __init__(self, env, drone, basestation, channel):
        self.env = env
        self.drone = drone
        self.basestation = basestation
        self.channel = channel

    def run(self):
        times = self.env.time_grid()

        distance_m = []
        azimuth_rad = []
        elevation_rad = []
        array_gain_db = []
        pathloss_db = []
        rx_power_dbm = []
        snr_db = []
        capacity_bps = []

        for t in times:
            # Update drone position
            self.drone.update(t)

            # Compute channel metrics
            link = self.channel.compute_link(self.drone, self.basestation)

            distance_m.append(link["distance_m"])
            azimuth_rad.append(link["azimuth_rad"])
            elevation_rad.append(link["elevation_rad"])
            array_gain_db.append(link["array_gain_db"])
            pathloss_db.append(link["pathloss_db"])
            rx_power_dbm.append(link["rx_power_dbm"])
            snr_db.append(link["snr_db"])
            capacity_bps.append(link["capacity_bps"])

        return {
            "time": times,
            "distance_m": np.array(distance_m),
            "azimuth_rad": np.array(azimuth_rad),
            "elevation_rad": np.array(elevation_rad),
            "array_gain_db": np.array(array_gain_db),
            "pathloss_db": np.array(pathloss_db),
            "rx_power_dbm": np.array(rx_power_dbm),
            "snr_db": np.array(snr_db),
            "capacity_bps": np.array(capacity_bps),
        }
