PYTHON = uv run python3

run:
	$(PYTHON) main.py

# This is for plotting the geometry of different array types.
plot:
	$(PYTHON) main.py plot-geometry $(type) $(args)

plot-ula:
	$(PYTHON) main.py plot-geometry ula $(N)

plot-uca:
	$(PYTHON) main.py plot-geometry uca $(N)

plot-ura:
	$(PYTHON) main.py plot-geometry ura $(Nx) $(Ny)

plot-uha:
	$(PYTHON) main.py plot-geometry uha $(N)

plot-all-geometry:
	$(MAKE) plot-ula N=16
	$(MAKE) plot-uca N=16
	$(MAKE) plot-ura Nx=4 Ny=4
	$(MAKE) plot-uha N=16
	$(MAKE) plot-ula N=8
	$(MAKE) plot-uca N=8
	$(MAKE) plot-ura Nx=4 Ny=2
	$(MAKE) plot-uha N=8

# This is for plotting the beam patterns of different array types.
plot-beampattern:
	$(PYTHON) main.py plot-beampattern $(type) $(args)

plot-beampattern-ula:
	$(PYTHON) main.py plot-beampattern ula $(N)

plot-beampattern-uca:
	$(PYTHON) main.py plot-beampattern uca $(N)

plot-beampattern-ura:
	$(PYTHON) main.py plot-beampattern ura $(Nx) $(Ny)

plot-beampattern-uha:
	$(PYTHON) main.py plot-beampattern uha $(N)

plot-all-beampatterns:
	$(MAKE) plot-beampattern-ula N=16
	$(MAKE) plot-beampattern-uca N=16
	$(MAKE) plot-beampattern-ura Nx=4 Ny=4
	$(MAKE) plot-beampattern-uha N=16
	$(MAKE) plot-beampattern-ula N=8
	$(MAKE) plot-beampattern-uca N=8
	$(MAKE) plot-beampattern-ura Nx=4 Ny=2
	$(MAKE) plot-beampattern-uha N=8

simulate:
	$(PYTHON) main.py simulate $(type) $(args) \
		--duration $(duration) \
		--dt $(dt) \
		--speed $(speed) \
		--tx_power $(tx)

# Preset simulation run (ULA-8, 10s duration, dt=0.1, speed 5 m/s, tx=20 dBm)
simulate-default:
	$(PYTHON) main.py simulate ula 8 \
		--duration 10 \
		--dt 0.1 \
		--speed 5 \
		--tx_power 20

live-demo:
	streamlit run demo.py