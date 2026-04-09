# Star Chart Options for Project Hail Mary Map

We want a background star chart covering the sky region containing the key stars
from *Project Hail Mary*: Tau Ceti, Epsilon Eridani, 40 Eridani, Sirius, and
WISE-0855. The chart should include constellation markings to help beginners,
not too many stars, and must permit additions/modifications (with credit OK).

## Why a pre-existing single chart is unlikely

These five stars span a wide, unusual strip of sky:

| Star | RA | Dec | Constellation |
|---|---|---|---|
| Tau Ceti | ~1h 44m | ~-16° | Cetus |
| Epsilon Eridani | ~3h 32m | ~-10° | Eridanus |
| 40 Eridani | ~4h 15m | ~-8° | Eridanus |
| Sirius | ~6h 45m | ~-17° | Canis Major |
| WISE-0855 | ~8h 55m | ~-7° | Hydra |

That is roughly **120° of right ascension** (RA 1h–9h), crossing Cetus,
Eridanus, Orion, Lepus, Canis Major, Monoceros, and Hydra. No standard
single-constellation chart covers this strip, so a pre-existing chart for
exactly this region is unlikely.

---

## Option 1: `starplot` (Python, MIT license) — CHOSEN

- **URL:** <https://starplot.dev/> · [GitHub](https://github.com/steveberardi/starplot)
- **License:** MIT — very permissive, no copyleft, commercial use OK, credit not required
- **SVG output:** Yes, native
- **Constellation lines:** Yes, built-in
- **Region charts:** Yes — specify RA/Dec center and field of view
- **Install:** `pip install starplot` (fits existing venv)

**Pros:**
- MIT license (most permissive of the options)
- Pure Python, pip-installable — fits the existing project
- SVG output that can be layered with additional markings
- Active project with good documentation
- Can generate exactly the RA/Dec region needed

**Cons:**
- Not a pre-existing finished chart; requires a short Python script (~20–30 lines) to generate the base
- Output style is programmatic rather than hand-crafted

---

## Option 2: `star-charter` by Dominic Ford (GPL-3, C tool)

- **URL:** [dcf21/star-charter on GitHub](https://github.com/dcf21/star-charter)
- **License:** GPL-3 — derived works must also be GPL-3
- **SVG output:** Yes (also PDF, PNG, EPS)
- **Constellation lines:** Yes

**Pros:**
- Very polished, professional-looking output
- Highly configurable RA/Dec region bounds
- Milky Way background shading available

**Cons:**
- Requires C build toolchain (CMake) and ~500MB data download
- GPL-3 copyleft could restrict downstream use of derived works
- More setup overhead than a Python pip install

---

## Option 3: Wikimedia Commons per-constellation SVGs (CC-BY-SA 4.0)

Individual SVG maps for each constellation:

- [Eridanus constellation map](https://commons.wikimedia.org/wiki/File:Eridanus_constellation_map.svg)
- [Cetus constellation map](https://commons.wikimedia.org/wiki/File:Cetus_constellation_map.svg)
- [Canis Major constellation map](https://commons.wikimedia.org/wiki/File:Canis_Major_constellation_map.svg)

- **License:** CC-BY-SA 4.0 — credit required; **derivatives must also be CC-BY-SA** (share-alike)
- **SVG output:** Already SVG, ready-made
- **Constellation lines:** Yes

**Pros:**
- No code required; charts already exist
- Authoritative IAU-style appearance

**Cons:**
- Individual per-constellation maps at different scales — would need to combine ~4 maps, re-project to common coordinates
- The CC-BY-SA share-alike requirement propagates to any derived work
- Significant Inkscape work to merge and align maps before adding markers

---

## Option 4: IAU Office of Astronomy for Education (CC-BY 4.0)

- **URL:** [IAU OAE constellation diagrams](https://astro4edu.org/iau-constellation-diagrams/)
- **License:** CC-BY 4.0 — credit required, **no share-alike** (more permissive than CC-BY-SA)
- **SVG output:** Yes

**Pros:**
- CC-BY 4.0 is more permissive than CC-BY-SA (no copyleft on derivatives)
- Official IAU source, high quality

**Cons:**
- Same structural problem as Option 3: individual per-constellation maps, not a regional strip
- Would require the same manual merging/re-projection work

---

## Recommendation summary

**Use Option 1 (`starplot`, MIT).** A short Python script generates the base SVG
covering exactly the needed region with constellation lines, then arrows and
labels can be overlaid programmatically or added in Inkscape. The MIT license
imposes no restrictions on the derived work.
