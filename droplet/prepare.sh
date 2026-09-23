#!/bin/bash
set -e
rm -r constant/polyMesh

python3 make_cap_v2.py
mkdir -p constant/triSurface
mv dropletCap.stl constant/triSurface/

blockMesh &> log.blockMesh
surfaceFeatureExtract &> log.surfaceFeatureExtract
snappyHexMesh -overwrite  &> log.snappyHexMesh
createPatch &> log.createPatch
extrudeMesh &> log.extrudeMesh
