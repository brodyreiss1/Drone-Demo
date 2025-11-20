import argparse
import numpy as np

from utils.coords import get_coords

from plots.geometry import plot_geometry
from plots.beam_pattern import plot_polar, plot_heatmap
from plots.simulation import plot_simulation_metrics

from beamforming.beam_pattern import sweep_2d, sweep_azimuth

from simulation.environment import Environment
from simulation.drone import Drone
from simulation.basestation import BaseStation
from simulation.channel import Channel
from simulation.simulator import Simulator
from simulation.paths import straight_path


def main():
    parser = argparse.ArgumentParser(description="Antenna Array Simulator")
    sub = parser.add_subparsers(dest="command")

    pg = sub.add_parser("plot-geometry", help="Plot array geometry")
    pg.add_argument("array_type", choices=["ula", "uca", "uha", "ura"])
    pg.add_argument("params", nargs="*", help="Array parameters")

    bg = sub.add_parser("plot-beampattern", help="Plot beam patterns")
    bg.add_argument("array_type", choices=["ula", "uca", "uha", "ura"])
    bg.add_argument("params", nargs="*", help="Array parameters")

    sim = sub.add_parser("simulate", help="Run simulation")
    sim.add_argument("array_type", choices=["ula", "uca", "uha", "ura"])
    sim.add_argument("params", nargs="*", help="Array parameters")
    sim.add_argument("--duration", type=float, default=10.0,
                     help="Simulation duration in seconds")
    sim.add_argument("--dt", type=float, default=0.1)
    sim.add_argument("--speed", type=float, default=5.0)
    sim.add_argument("--tx_power", type=float, default=20.0)

    args = parser.parse_args()

    if args.command == "plot-geometry":
        coords = get_coords(args.array_type.lower(), args.params)

        param_str = "_".join(args.params)
        save_path = f"outputs/geometry/{args.array_type}_{param_str}.png"
        plot_geometry(
            coords,
            title=f"{args.array_type.upper()} Geometry",
            save_path=save_path
        )

    if args.command == "plot-beampattern":
        arr_type = args.array_type.lower()
        coords = get_coords(arr_type, args.params)

        param_str = "_".join(args.params)

        if arr_type == "ula":
            phis, af_values = sweep_azimuth(coords)
            save_path_az = f"outputs/beampattern/{arr_type}_{param_str}_azimuth.png"
            plot_polar(
                phis,
                af_values,
                title=f"{args.array_type.upper()} Beam Pattern",
                save_path=save_path_az
            )
        else:
            thetas, phis, AF = sweep_2d(coords)
            save_path_heatmap = f"outputs/beampattern/{arr_type}_{param_str}_heatmap.png"
            plot_heatmap(
                thetas,
                phis,
                AF,
                title=f"{args.array_type.upper()} Beam Pattern Heatmap",
                save_path=save_path_heatmap
            )

    if args.command == "simulate":
        arr_type = args.array_type.lower()
        coords = get_coords(arr_type, args.params)

        env = Environment(dt=args.dt, duration=args.duration)
        path = straight_path(
            start=[0.0, -50.0, 20.0],
            direction=[1.0, 0.0, 0.0],
            speed=args.speed
        )
        drone = Drone(
            path_fn=path,
            tx_power_dbm=args.tx_power
        )
        basestation = BaseStation(
            position=np.array([0.0, 0.0, 0.0]),
            array_coords=coords
        )
        channel = Channel()

        simulator = Simulator(env, drone, basestation, channel)
        results = simulator.run()

        plot_simulation_metrics(
            results,
            save_prefix=f"outputs/simulation/{arr_type}"
        )


if __name__ == "__main__":
    main()
