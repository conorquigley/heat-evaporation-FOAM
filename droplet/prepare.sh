#!/bin/bash
rm -r constant/polymesh
blockMesh &> log.blockMesh

# -----------------------------
# Prepare 0 file for initial conditions
# -----------------------------
cp -r 0.orig 0

snappyHexMesh -overwrite
rm -f 0/cellLevel 0/pointLevel
extrudeMesh
python replace_axis.py
setFields &> log.setFields
