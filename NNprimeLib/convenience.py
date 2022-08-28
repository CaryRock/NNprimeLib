import numpy as np
import os

def loadNNprimeFile(phile):
    with open(phile, "r") as f:
        _ = f.readline()
        mass, theta = f.readline().split()
        mass = float(mass)
        theta = float(theta)
        header = f.readline()

        data = np.loadtxt(phile, skiprows = 3, comments = "#")

        return mass, theta, header, data
    f.close()

def loadNNprimeSummary(phile):
    with open(phile, "r") as f:
        _ = f.readline()    # Mulch the header
        mass = float(phile[8:-7])
        data = np.loadtxt(phile, comments = "#")

        return mass, data

def get_list_of_directories():
    dirs = []
    raw = os.listdir()  # Returns list of all items in the directory

    # Checks each item in `raw` for being a directory
    for r in raw:
        if os.path.isdir(r):
            dirs.append(r)

    return dirs

def get_raw_list_of_files(dir):
    file_list = []
    os.chdir(dir)
    raw = os.listdir()

    for r in raw:
        if not os.path.isdir(r):
            file_list.append(r)

    return file_list

def get_list_of_data_files(raw_list, ext = '.dat'):
    refined_list = []
    for r in raw_list:
        if r.endswith(ext):
            refined_list.append(r)

    return refined_list

