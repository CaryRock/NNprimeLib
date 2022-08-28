#!/usr/bin/env python

from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.rcParams['figure.figsize'] = [10, 10]
plt.rcParams["savefig.format"] = "pdf"

def get_list_of_files(loc = '.'):
    file_list = []
    folder = glob(loc + "/*.datsum")
    length = len(folder)
    file_list = [None] * length

    for index, phile in enumerate(folder):
        file_list[index] = phile

    return file_list

def plotter(data, mass, c_values, log):
    if log == True:
        plt.scatter(mass * np.ones_like(data), data, c = c_values)
    else:
        plt.scatter(mass * np.ones_like(data), 180 / np.pi * data, c = c_values)

def set_plotter_props(material, log, element):
    #plt.title(f"{material} " + r"$\Psi(0) = \left( 2\theta^2, 1-2\theta^2 \right)^T$ ; $\rho_{{11}}$")
    plt.title(f"{material} " + r"$\Psi(0) = \left( 0, 1 \right)$ ; $\rho_{{{}}}$".format(element))
    plt.axvline(167e-9, c = "white")
    
    if log == False:
        plt.yscale("linear")
        plt.ylim(top=44.9, bottom=0.0)
        plt.ylabel(r"$\theta_0$ (deg)")
    else:
        plt.yscale("log")
        plt.ylabel(r"$\theta_0$ (rad)")
    
    plt.xscale("log")
    plt.xlabel(r"$\Delta m$ (eV)")
    plt.colorbar()

def main():
    material = "D2O"
    directory = material + "/"
    file_name = "summary_"
    file_list = get_list_of_files(directory)

    masses = np.zeros(len(file_list))
    
    # rho_nn    rho_mn  rho_nm  rho_mm
    #    3         4       5       6 
    header = ["x", "theta", "distance", r"$\rho_{{nn}}$", r"$\rho_{{nn'}}$", r"$\rho_{{n'n}}$", r"$\rho_{{n'n'}}$"]
    rho1 = 3
    rho2 = 6
    dirlength = len(directory)
    extension = 7
    namelength = len(file_name)
    log = True

    for index, ffile in enumerate(file_list):
        # Find the length of each file, then create 
        masses[index] = float(ffile[dirlength + namelength:-extension])  # Get the masses
        data = np.loadtxt(ffile, dtype="float", comments = "#")
        plotter(data[:,1], masses[index], data[:,rho1], log)

    set_plotter_props(material, log)
    plt.savefig(f"{material}_log_11")
    plt.clf()
    #plt.show()

    for index, ffile in enumerate(file_list):
        masses[index] = float(ffile[dirlength + namelength:-extension])  # Get the masses
        data = np.loadtxt(ffile, dtype="float", comments = "#")
        plotter(data[:,1], masses[index], data[:,rho1], not log)

    set_plotter_props(material, not log)
    plt.savefig(f"{material}_linear_11")
    plt.clf()
    #plt.show()

    for index, ffile in enumerate(file_list):
        # Find the length of each file, then create 
        masses[index] = float(ffile[dirlength + namelength:-extension])  # Get the masses
        data = np.loadtxt(ffile, dtype="float", comments = "#")
        plotter(data[:,1], masses[index], data[:,rho2], log)

    set_plotter_props(material, log)
    plt.savefig(f"{material}_log_22")
    plt.clf()
    #plt.show()

    for index, ffile in enumerate(file_list):
        # Find the length of each file, then create 
        masses[index] = float(ffile[dirlength + namelength:-extension])  # Get the masses
        data = np.loadtxt(ffile, dtype="float", comments = "#")
        plotter(data[:,1], masses[index], data[:,rho2], not log)

    set_plotter_props(material, not log)
    plt.savefig(f"{material}_linear_22")
    plt.clf()
    #plt.show()

if __name__ == "__main__":
    main()