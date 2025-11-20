import matplotlib.pyplot as plt
import os


def plot_simulation_metrics(results, save_prefix=None):
    t = results["time"]
    dist = results["distance_m"]
    snr = results["snr_db"]
    cap = results["capacity_bps"]

    # Distance
    plt.figure()
    plt.plot(t, dist)
    plt.xlabel("Time (s)")
    plt.ylabel("Distance (m)")
    plt.title("Drone Distance")
    plt.grid(True)
    if save_prefix:
        os.makedirs(os.path.dirname(save_prefix), exist_ok=True)
        plt.savefig(f"{save_prefix}_distance.png", dpi=300)

    # SNR
    plt.figure()
    plt.plot(t, snr)
    plt.xlabel("Time (s)")
    plt.ylabel("SNR (dB)")
    plt.title("SNR Over Time")
    plt.grid(True)
    if save_prefix:
        os.makedirs(os.path.dirname(save_prefix), exist_ok=True)
        plt.savefig(f"{save_prefix}_snr.png", dpi=300)

    # Capacity
    plt.figure()
    plt.plot(t, cap)
    plt.xlabel("Time (s)")
    plt.ylabel("Capacity (bps)")
    plt.title("Shannon Capacity")
    plt.grid(True)
    if save_prefix:
        os.makedirs(os.path.dirname(save_prefix), exist_ok=True)
        plt.savefig(f"{save_prefix}_capacity.png", dpi=300)
