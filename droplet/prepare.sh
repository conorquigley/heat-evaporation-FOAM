#!/bin/bash
set -e
rm -r constant/polyMesh

python3 make_cap_v2.py
mkdir -p constant/triSurface
mv dropletCap.stl constant/triSurface/

blockMesh &> log.blockMesh
surfaceFeatureExtract &> log.surfaceFeatureExtract
snappyHexMesh &> log.snappyHexMesh
# -----------------------------
# Prepare 0 file for initial conditions
# -----------------------------
cp -r 0.orig 0

