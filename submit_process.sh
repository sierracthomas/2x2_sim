#!/bin/bash

#SBATCH -N 1
#SBATCH -C cpu
#SBATCH -q regular
#SBATCH -J nu_e
#SBATCH -A dune
#SBATCH -t 15:00:00

cd /global/homes/s/sthoma31/retry/2x2_sim

source run_sequence.txt
