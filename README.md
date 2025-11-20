## Setup environment

### Installing UV (Package Manager)
Install the package manager uv. This sets us up on the same python version and with the same versions of everything. 
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installing Packages
To install all of the relavent python packages, running the following command will install all of the dependencies.
```shell
uv sync
```

### Going into the virtual environment (on MacOS)
```shell
source .venv/bin/activate
```

### Plotting the Array Geometry
There is a Makefile where you can run the following commands to plot the array geometry

| Array Type | Make Command | Example |
|-----------|--------------|---------|
| **Uniform Linear Array (ULA)** | `make plot-ula N=<elements>` | `make plot-ula N=16` |
| **Uniform Circular Array (UCA)** | `make plot-uca N=<elements>` | `make plot-uca N=12` |
| **Uniform Rectangular Array (URA)** | `make plot-ura Nx=<cols> Ny=<rows>` | `make plot-ura Nx=4 Ny=4` |
| **Uniform Hexagonal Array (UHA)** | `make plot-uha N=<elements>` | `make plot-uha N=8` |

---

The plots are saved to `outputs/geometry/<array>_<params>.png`

### Plotting Beam Patterns
You can also plot the beam patterns for each array type using the Makefile:

| Array Type | Make Command | Example |
|-----------|--------------|---------|
| **Uniform Linear Array (ULA)** | `make plot-beampattern-ula N=<elements>` | `make plot-beampattern-ula N=16` |
| **Uniform Circular Array (UCA)** | `make plot-beampattern-uca N=<elements>` | `make plot-beampattern-uca N=16` |
| **Uniform Rectangular Array (URA)** | `make plot-beampattern-ura Nx=<cols> Ny=<rows>` | `make plot-beampattern-ura Nx=4 Ny=4` |
| **Uniform Hexagonal Array (UHA)** | `make plot-beampattern-uha N=<elements>` | `make plot-beampattern-uha N=8` |

To generate a set of sample beam pattern plots for several configurations:

```shell
make plot-all-beampatterns
```

Beam pattern plots are saved under `outputs/beampattern/` with filenames like `<array>_<params>_azimuth.png` or `<array>_<params>_heatmap.png`.

### Running Simulations
The simulator lets you move a drone along a path and compute distance, SNR, and capacity over time for a given array configuration.

You can run a simulation for any array type with:

```shell
make simulate type=<ula|uca|ura|uha> args="<array params>" duration=<seconds> dt=<seconds> speed=<m/s> tx=<tx power dBm>
```

Examples:

```shell
# ULA with 8 elements, 10 s duration, dt=0.1, speed 5 m/s, 20 dBm
make simulate type=ula args="8" duration=10 dt=0.1 speed=5 tx=20

# URA with 4x4 elements
make simulate type=ura args="4 4" duration=10 dt=0.1 speed=5 tx=20
```

There is also a preset default simulation:

```shell
make simulate-default
```

This runs a ULA-8 simulation for 10 seconds with `dt=0.1`, speed `5 m/s`, and transmit power `20 dBm`.

Simulation plots (distance, SNR, and capacity vs time) are saved under `outputs/simulation/` with filenames starting with the array type (e.g., `ula_distance.png`, `ula_snr.png`, `ula_capacity.png`).