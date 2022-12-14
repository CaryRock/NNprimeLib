#!/usr/bin/env python
# Reads in data files (specifically, those ending in *.dat) that match a given
# input mass. Generates an output file corresponding to the input mass of all
# the final values of the files.
import numpy as np
import os
import sys
from NNprimeLib import convenience as nnpc
from concurrent.futures import ProcessPoolExecutor as ppe

# This application should read through each directory inside, find all the 
# appropriate files (currently, those in .dat, but this may change), and
# do some analysis on them (namely, pick out the last line in the file, 
# which is assumed to be the end point - a more clever analysis method could
# be developed, but isn't necessary at the moment).

def analyze_file(dir: str) -> int:
    num_data_files      = 0
    num_columns_in_file = 7
    header              = []    
    mass                = 0.0
    theta               = 0.0
    os.chdir(dir)   # Move to directory containing desired files

    raw_file_list = nnpc.get_raw_list_of_files(".") # Retrieve list of files
    file_list = nnpc.get_list_of_data_files(raw_file_list)
    # List in hand, count number of files to get size
    num_data_files = len(file_list)
    last_vals = np.zeros(shape=(num_data_files, num_columns_in_file), dtype='float')

    for index, phil in enumerate(file_list):
        mass, theta, header, data = nnpc.loadNNprimeFile(phil)
            # Reads the file, returns the pertinent parts
        last_vals[index, 0] = theta
        last_vals[index, 1:] = data[-1]

    # TODO: Implement method to sort the output so that it doesn't have to happen
    #       during plotting

    # Once all the files have been processed, write out summary report in 
    # each of the directories
    with open(f"summary_{mass}.datsum", "w") as f:

        f.write(f"#theta\t {header[1:]}")   # Write the header

        for i in range(num_data_files):
            for j in range(num_columns_in_file):
                f.write(f"{last_vals[i][j]}\t")
            f.write("\n")
    
    return 0
    
def main():
    # Import only the files that end in .dat
    head    = os.getcwd()   # Returns directory of invocation
    
    # Get list of directories
    dir_list = nnpc.get_list_of_directories()
    results = len(dir_list)*[None]  # Smart error checking would make this some
        # relate index to folder for verification - probably a dictionary

    if len(sys.argv) == 1:  # Nothing specified
        #TODO: Need MPI pool to be constrained by SLURM
        # OR
        # len(dir_list) % (something reasonable for sharing ISAAC - 20?)
        with ppe(max_workers = 20) as executor:
            results = executor.map(analyze_file, dir_list)
        #results = map(analyze_file, dir_list)

if __name__ == "__main__":
    main()
