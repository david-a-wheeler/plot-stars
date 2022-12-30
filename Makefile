
all: hail-mary.svg

hail-mary.svg: plot-stars nearby.csv
	./plot-stars

install_libraries:
	pip3 install pandas numpy matplotlib
