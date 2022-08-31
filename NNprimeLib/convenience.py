import numpy as np
import os

def loadNNprimeFile(phile: str) -> [float, float, list, np.array]:
    with open(phile, "r") as f:
        _ = f.readline()
        mass, theta = f.readline().split()
        mass = float(mass)
        theta = float(theta)
        header = f.readline()

        data = np.loadtxt(phile, skiprows = 3, comments = "#")

    return mass, theta, header, data

def loadNNprimeSummary(phile: str) -> float:
    with open(phile, "r") as f:
        _ = f.readline()    # Mulch the header
        mass = float(phile[8:-7])
        data = np.loadtxt(phile, comments = "#")

        return mass, data

def get_list_of_directories() -> list:
    dirs = []
    raw = os.listdir()  # Returns list of all items in the directory

    # Checks each item in `raw` for being a directory
    for r in raw:
        if os.path.isdir(r):
            dirs.append(r)

    if len(dirs) == 0:
        dirs.append(os.getcwd())
        
    return dirs

def get_raw_list_of_files(dir: str) -> list:
    file_list = []
    os.chdir(dir)
    raw = os.listdir()

    for r in raw:
        if not os.path.isdir(r):
            file_list.append(r)

    return file_list

def get_list_of_data_files(raw_list: list, ext: str = '.dat') -> list:
    refined_list = []
    for r in raw_list:
        if r.endswith(ext):
            refined_list.append(r)

    return refined_list

