
VENV = .venv

# By default we use the *virtual environment* Python,
# not the *system* Python. As a result, our processing will always
# use the virtual environment.
PYTHON = $(VENV)/bin/python3

all: hail-mary.svg

hail-mary.svg: plot-stars nearby.csv $(VENV)/bin/activate
	$(PYTHON) ./plot-stars

# Activate Python virtual environment
$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install pandas numpy matplotlib

clean:
	rm -f hail-mary.svg
