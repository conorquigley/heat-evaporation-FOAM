#!/bin/bash
rm -r constant/polymesh
blockMesh &> log.blockMesh

# -----------------------------
# Prepare 0 file for initial conditions
# -----------------------------
cp -r 0.orig 0

rm -f 0/cellLevel 0/pointLevel
setFields &> log.setFields
