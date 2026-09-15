#!/bin/bash

decomposePar > log.decomposePar 2>&1
mpirun -np 14 interFoam -parallel > log.interFoam 
reconstructPar > log.reconstructPar 2>&1
