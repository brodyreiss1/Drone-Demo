import streamlit as st
import numpy as np
import sys
import os
import matplotlib.pyplot as plt

# Add the current directory to sys.path so we can import local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.coords import get_coords
from simulation.environment import Environment
from simulation.drone import Drone
from simulation.basestation import BaseStation
from simulation.channel import Channel
from simulation.simulator import Simulator
from simulation.paths import straight_path

st.set_page_config(page_title="UAV Beamforming Demo", layout="wide")

st.title("UAV Beamforming Simulation Demo")
st.markdown("##### Created by Brody Reiss and Brady Lauritsen")
st.markdown("""
This interactive demo simulates the performance of different antenna array configurations 
for a drone-to-ground communication link. Adjust the parameters in the sidebar to see 
how they impact Signal-to-Noise Ratio (SNR) and Channel Capacity.
""")

# --- Sidebar Configuration ---
st.sidebar.header("1. Array Configuration")
array_type = st.sidebar.selectbox(
    "Array Geometry",
    ("ULA", "UCA", "URA", "UHA"),
    index=2 # Default to URA
)

params = []
if array_type == "ULA":
    N = st.sidebar.slider("Number of Elements (N)", 2, 64, 16)
    params = [str(N)]
elif array_type == "UCA":
    N = st.sidebar.slider("Number of Elements (N)", 4, 64, 16)
    params = [str(N)]
elif array_type == "URA":
    col1, col2 = st.sidebar.columns(2)
    Nx = col1.slider("Nx", 2, 16, 4)
    Ny = col2.slider("Ny", 2, 16, 4)
    params = [str(Nx), str(Ny)]
    st.sidebar.text(f"Total Elements: {Nx * Ny}")
elif array_type == "UHA":
    N_side = st.sidebar.slider("Hexagon Side Elements", 2, 8, 3)
    params = [str(N_side)]
    # Calculate total elements for display: 3n(n-1) + 1
    total_elems = 3 * N_side * (N_side - 1) + 1
    st.sidebar.text(f"Total Elements: {total_elems}")

st.sidebar.header("2. Drone Flight Parameters")
speed = st.sidebar.slider("Drone Speed (m/s)", 1.0, 50.0, 15.0)
altitude = st.sidebar.slider("Altitude (m)", 10.0, 500.0, 100.0)
duration = st.sidebar.slider("Simulation Duration (s)", 5.0, 60.0, 20.0)

st.sidebar.header("3. Link Budget")
tx_power = st.sidebar.slider("Tx Power (dBm)", 0.0, 40.0, 20.0)


# --- Run Simulation ---
# We use a button or just run it reactively. Reactive is better for demos.
# st.sidebar.markdown("---")

try:
    # 1. Setup Geometry
    coords = get_coords(array_type.lower(), params)

    # 2. Setup Environment & Path
    env = Environment(dt=0.1, duration=duration)
    
    # Create a path that flies over the base station
    # Starting at x=-distance, y=0, z=altitude
    # Flying towards +x
    start_x = -(speed * duration) / 2
    path = straight_path(
        start=[start_x, 0.0, altitude],
        direction=[1.0, 0.0, 0.0],
        speed=speed
    )

    # 3. Setup Components
    drone = Drone(path_fn=path, tx_power_dbm=tx_power)
    basestation = BaseStation(position=np.array([0.0, 0.0, 0.0]), array_coords=coords)
    channel = Channel()

    # 4. Run Simulator
    simulator = Simulator(env, drone, basestation, channel)
    results = simulator.run()

    # --- Display Results ---

    # Metrics Row
    avg_snr = np.mean(results["snr_db"])
    min_snr = np.min(results["snr_db"])
    avg_cap = np.mean(results["capacity_bps"]) / 1e6 # Mbps
    
    st.subheader("Performance Over Time")

    col_dist1, col_dist2 = st.columns([1, 1])
    with col_dist1:
        st.write("Flight Path vs Distance")
        fig, ax = plt.subplots(figsize=(10, 3))
        ax.plot(results["time"], results["distance_m"], label="Distance (m)", color="orange")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Distance (m)")
        ax.grid(True)
        st.pyplot(fig)
    
    with col_dist2:
        st.write("Key Metrics")
        m_col1, m_col2 = st.columns(2)
        m_col1.metric("Avg SNR", f"{avg_snr:.2f} dB")
        m_col2.metric("Min SNR", f"{min_snr:.2f} dB", help="Lowest signal quality during flight")
        
        m_col3, m_col4 = st.columns(2)
        m_col3.metric("Avg Capacity", f"{avg_cap:.2f} Mbps")
        m_col4.metric("Array Elements", len(coords))

    tab1, tab2, tab3 = st.tabs(["Geometry", "Capacity", "SNR Analysis"])
    
    # Plots
    with tab1:
        st.write("Array Geometry (Top Down)")
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.scatter(coords[:, 0], coords[:, 1], color="red", marker="x")
        ax.set_aspect('equal')
        ax.grid(True)
        ax.set_xlabel("x (m)")
        ax.set_ylabel("y (m)")
        st.pyplot(fig)

    with tab2:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(results["time"], results["capacity_bps"] / 1e6, label="Capacity (Mbps)", color="#28a745", linewidth=2)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Capacity (Mbps)")
        ax.grid(True, alpha=0.3)
        ax.legend()
        st.pyplot(fig)

    with tab3:
        # Create a custom plot for SNR
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(results["time"], results["snr_db"], label="SNR (dB)", color="#007bff", linewidth=2)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("SNR (dB)")
        ax.grid(True, alpha=0.3)
        ax.legend()
        st.pyplot(fig)
        
        st.info("Note how the SNR changes as the drone passes overhead (t=0 is not necessarily overhead in this path setup, check the distance plot).")

except Exception as e:
    st.error(f"An error occurred during simulation: {e}")
    st.write("Please check your parameters.")

