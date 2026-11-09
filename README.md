# 2D Droplet Evaporative Flux
Domain and set-up for 2D spherical cap droplet evaporation flux simulation.

The droplet directory contains all that is required to recreate the simulation.

## Requirements

- OpenFOAM v2412 (ESI-OpenCFD)
- Python 3.11+ with numpy; tested with Python 3.14.4 and numpy 2.3.5
- ParaView (optional, for visualisation)
- Tested on Ubuntu 26.04


## Quick start


cd droplet
./prepare.sh   # generate geometry and mesh, set up the case
./run.sh       # run the simulation

To view the results, open `droplet/droplet.foam` in ParaView

To reset the case and start again from scratch:

```bash
./clean.sh
```

## Repository structure


```
.
├── README.md
└── droplet/
    ├── make_cap_v2.py   Generates the spherical-cap surface (constant/triSurface/dropletCap.stl)
    ├── prepare.sh       Geometry, meshing and case set-up; copies orig/ to 0/
    ├── run.sh           Runs the simulation
    ├── clean.sh         Resets the case to its pre-run state
    ├── droplet.foam     Empty file for opening the case in ParaView
    ├── orig/            Template initial and boundary conditions (T)
    ├── constant/        Physical properties and surface geometry; the mesh is generated here
    └── system/          Mesh, solver and run-control dictionaries
```

## Simulation parameters

| Parameter | Value | Location |
|---|---|---|
| Droplet radius | [0.003m] | `droplet/make_cap_v2.py` |
| Contact angle | [45 deg ] | `droplet/make_cap_v2.py` |
| Diffusivity | [2.42x10^-5] | `droplet/constant/transportProperties` |
| Time step, end time | [0.1,30 s] | `droplet/system/controlDict` |
