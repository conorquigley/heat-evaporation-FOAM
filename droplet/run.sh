#!/bin/bash
laplacianFoam &> log.laplacianFOAM
postProcess -fields '(flux)' 2>&1 | tee log.postProcess
