
# ML Dataset Generation branch

Before running jobs, edit `submit_process.sh` to point to your `2x2-sim` directory. Edit `run_sequence.txt` to be sure that the files are placed in your desired SCRATCH directory. Each step will generate N files (where n is in the sequence from 0 to 25). 

To run a job, do the following:

`sbatch submit_process.sh`

To check the job's status, type `squeue -u <username>`. 

If you would like to edit the interactions in the genie step, change the `gevgen_fnal` arguments in `2x2_sim/run-genie/run_genie.sh`. For more information about arguments, see section 5.3.1 in [the Genie documentation](https://genie-docdb.pp.rl.ac.uk/DocDB/0000/000002/007/1510.05494v1.pdf). Note that the command on line 57 is `gevgen`, not `gevgen_fnal`. 

The output files should be located in your `$ARCUBE_OUTDIR_BASE/run-convert2h5/Tutorial.convert2h5/EDEPSIM_H5/0000000/`. This will contain a number of `.hdf5` files which should be transferred to its-og. These hdf5 files are the input to the array generator code in `neutrino_interaction_CNN`. 

# Other dataset generation branches

The other branches on this fork have code that might work for Argon-40 de-excitation gammas and argon-39 beta decay. To swap to a different branch, try:

`git checkout argon40-gamma`

NOTE: git won't let you swap branches without "stashing" or "committing" your changes. See [Git documentation](https://git-scm.com/docs) for more information.

The `argon40-gamma` `run_sequence.txt` file doesn't contain a genie step, so it instead will generate the de-excitation gammas from the `run-edep-sim` step. The changes should be made in this macro file `run-edep-sim/macros/2x2_beam.mac`. 


# 2x2_sim
Wrappers for ArgonCube 2x2 simulation designed to be run at NERSC.

Support for other computing clusters/environments using Singularity is now available and is configured by environment variable(s). Certain parts of the simulation chain (e.g. edep-sim) require large input files and need to be downloaded from NERSC or regenerated.

The repository wiki has a variety of useful information related to running and using the 2x2 simulation:

+ A tutorial on how to run the simulation can be found at [Tutorial on running 2x2_sim](https://github.com/DUNE/2x2_sim/wiki/Tutorial-on-running-2x2_sim)
+ Information on the data/variables inside the different output files can be found at [File data definitions](https://github.com/DUNE/2x2_sim/wiki/File-data-definitions)

Additional information may be found on the [ND-Prototype Analysis page(s)](https://wiki.dunescience.org/wiki/ND_Prototype_Analysis) on the DUNE wiki.

## Copyright and Licensing
Copyright © 2023 FERMI NATIONAL ACCELERATOR LABORATORY for the benefit of the DUNE Collaboration.

This repository, and all software contained within, is licensed under
the Apache License, Version 2.0 (the "License"); you may not use this
file except in compliance with the License. You may obtain a copy of
the License at

    http://www.apache.org/licenses/LICENSE-2.0

Copyright is granted to FERMI NATIONAL ACCELERATOR LABORATORY on behalf
of the Deep Underground Neutrino Experiment (DUNE). Unless required by
applicable law or agreed to in writing, software distributed under the
License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for
the specific language governing permissions and limitations under the
License.
