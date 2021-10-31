# plot-stars

This plots nearby star systems as an XYZ chart.
By default it creates a modified plot showing the stars
and connections related to the novel *Project Hail Mary*.
I may eventually change the default to just show nearby stellar systems.

The nearby star data is from
[Wikipedia's list of nearest stars](https://en.wikipedia.org/wiki/List_of_nearest_stars_and_brown_dwarfs)
the list of all known stars and brown dwarfs
(including sub-brown dwarfs)
within 5.0 parsecs (16.3 light-years) of the Solar System.
I use the word "star" here, but note that this includes rogue planets
like WISE 0855−0714 (which has more mass than Jupiter but not enough
mass to fuse atoms).
It was converted to CSV by
[Convert Wiki Tables to CSV](https://wikitable2csv.ggor.de/).

The plot takes the usual coordinate system used by astronomers,
converts them into XYZ format, and then plots the result.
Astronomers typically locate objects by reporting their
right ascension (angle reported as a fraction of 24-hour clock)
and declination (angle higher than the celestial equator).
We convert these values to XYZ cartesian coordinates using standard
coordinate transforms; for more information, see
["Putting Your Stars in Their Places" by Greg Scalise (2003)](http://fmwriters.com/Visionback/Issue14/wbputtingstars.htm).

The main code is in `plot-stars`.
The code is implemented using widely-used data analysis tools, specifically
Python3, pandas, numpy, and matplotlib.
You can run it yourself by installing `python3` and then running:

> pip3 install pandas numpy matplotlib

The code itself is licensed under GPL version 2+.
Resulting images are licensed under
[Creative Commons Attribution (CC-BY) version 3.0 or later](https://creativecommons.org/licenses/by/3.0/us/.)

