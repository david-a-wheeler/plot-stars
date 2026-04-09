# Makefile to plot & create sky chart for Project Hail Mary
# David A. Wheeler

# We use Python Virtual Environments (venvs) so our library downloads
# won't mess up other Python programs on this system.
VENV = .venv

# By default we use the *virtual environment* Python,
# not the *system* Python.
# Thus our processing will always use the virtual environment.
PYTHON = $(VENV)/bin/python3

# These are the images we'll generate
SVGS = hail-mary.svg hail-mary-sky.svg

all: $(SVGS)

# 3-D space-map: shows star positions relative to the Solar System.
# Depends on star_data.py because plot-stars imports TRANSMISSIONS from it.
hail-mary.svg: plot-stars star_data.py nearby.csv $(VENV)/bin/activate
	$(PYTHON) ./plot-stars

# Observer's sky chart: shows where the key stars appear in Earth's sky,
# with directed arcs for the Astrophage transmission path.
# Depends on star_data.py (shared data) and nearby.csv (WISE-0855 coords).
hail-mary-sky.svg: plot-sky star_data.py nearby.csv $(VENV)/bin/activate
	$(PYTHON) ./plot-sky

# Create the Python virtual environment and install all required packages.
# starplot is needed for plot-sky; pandas/numpy/matplotlib for plot-stars.
$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install pandas numpy matplotlib starplot

clean:
	rm -f hail-mary.svg hail-mary-sky.svg
