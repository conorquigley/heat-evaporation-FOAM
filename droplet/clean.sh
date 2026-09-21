#!/bin/bash
rm -f log.*
rm -r processor*
rm -r 0.0*
rm -r 0
rm -r postProcessing/
rm slurm*

cd constant/
rm -r polyMesh/*
rm triSurface/*
rm extendedFeatureEdgeMesh/*
