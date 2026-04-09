#!/usr/bin/env python3
# Shared story data for Project Hail Mary star maps.
#
# Copyright 2026 David A. Wheeler and plot-stars contributors
# SPDX-License-Identifier: GPL-2.0-or-later
#
# This module holds only the story-specific data that both plot-stars
# (the 3-D space map) and plot-sky (the observer's sky chart) need to
# share.  It intentionally contains NO star coordinates: those come from
# nearby.csv (the single authoritative source used by plot-stars) or from
# the starplot catalog (used by plot-sky to look up Hipparcos positions).

# ---------------------------------------------------------------------------
# WISE 0855-0714 system name
#
# The name uses a Unicode MINUS SIGN (U+2212, '−') rather than an ASCII
# hyphen-minus (U+002D, '-'), matching the character used in nearby.csv.
# Using the wrong character would silently break lookups in plot-stars.
# ---------------------------------------------------------------------------
WISE_NAME = 'WISE 0855\u22120714'   # 'WISE 0855−0714'

def patch_svg_responsive(filename):
    """Add style='max-width:100%;height:auto;' to the root <svg> element.

    This lets the SVG scale to fit the browser window when viewed directly
    while preserving the width/height attributes as intrinsic-size hints
    for HTML embedding.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        svg = f.read()
    svg = svg.replace('<svg ', '<svg style="max-width:100%;height:auto;" ', 1)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg)

# ---------------------------------------------------------------------------
# Directed Astrophage transmission arcs, source → destination.
#
# Names match the *short* system names that plot-stars derives from the
# 'System' column of nearby.csv by stripping parenthesised alternates and
# the § marker (e.g. "Tau Ceti (BD−16°295)" → "Tau Ceti").  The order
# follows the story's implied transmission sequence.
# ---------------------------------------------------------------------------
TRANSMISSIONS = [
    ('Tau Ceti',        'Epsilon Eridani'),
    ('Epsilon Eridani', 'Sirius'),
    ('Sirius',          WISE_NAME),
    (WISE_NAME,         'Solar System'),
    (WISE_NAME,         'Wolf 359'),
    (WISE_NAME,         'Lalande 21185'),
    (WISE_NAME,         'Ross 128'),
    ('Epsilon Eridani', '40 Eridani'),
]

# ---------------------------------------------------------------------------
# Hipparcos catalog IDs for the key story stars in the sky-chart region.
#
# plot-sky uses these to look up star positions in the starplot catalog so
# that arrow endpoints sit exactly on the dots that starplot draws, avoiding
# any coordinate drift between nearby.csv and the Hipparcos catalog.
#
# WISE 0855-0714 has no Hipparcos entry (it was discovered in 2014, long
# after the Hipparcos mission).  plot-sky reads its position from nearby.csv
# instead.
# ---------------------------------------------------------------------------
SKY_CHART_HIP = {
    'Tau Ceti':        8102,
    'Epsilon Eridani': 16537,
    '40 Eridani':      19849,
    'Sirius':          32349,
}

# ---------------------------------------------------------------------------
# Transmission arcs that fall within the sky-chart region.
#
# The sky chart covers RA ≈ 1h 44m – 8h 55m, Dec ≈ −17° to −7°.  The arcs
# to the Solar System, Wolf 359, Lalande 21185, and Ross 128 are excluded
# because those destinations lie in an entirely different part of the sky
# (see star-chart-options.md for the sky-area analysis).
# ---------------------------------------------------------------------------
SKY_CHART_TRANSMISSIONS = [
    ('Tau Ceti',        'Epsilon Eridani'),
    ('Epsilon Eridani', 'Sirius'),
    ('Sirius',          WISE_NAME),
    ('Epsilon Eridani', '40 Eridani'),
]
