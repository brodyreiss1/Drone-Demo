import matplotlib.pyplot as plt
import numpy as np
import os


def plot_polar(phases, af_values, title="", save_path=None):
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, projection='polar')
    ax.plot(phases, af_values / np.max(af_values))
    ax.set_title(title)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')


def plot_heatmap(thetas, phis, AF, title="", save_path=None):
    theta_deg = np.degrees(thetas)
    phi_deg = np.degrees(phis)

    plt.figure(figsize=(8, 6))
    plt.imshow(
        AF,
        extent=[phi_deg.min(), phi_deg.max(), theta_deg.min(), theta_deg.max()],
        aspect='auto',
        origin='lower'
    )
    plt.colorbar(label='Array Factor')
    plt.xlabel('Azimuth (degrees)')
    plt.ylabel('Elevation (degrees)')
    plt.title(title)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
