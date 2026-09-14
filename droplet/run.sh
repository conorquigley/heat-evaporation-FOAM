#!/bin/bash

decomposePar > log.decomposePar 2>&1
mpirun -np 14 interKistlerFoam -parallel > log.interKistlerFoam 
reconstructPar > log.reconstructPar 2>&1
