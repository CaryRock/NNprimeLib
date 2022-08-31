#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import pathlib as pl
import argparse as ap

plt.rcParams['figure.figsize'] = [10, 10]
plt.rcParams["savefig.format"] = "pdf"

def create_parser():
    parser = ap.ArgumentParser(description = "",
    formatter_class = ap.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-f", "--files", type = pl.Path, nargs = "+",
                        help = "Data files (*.dat) for plotting.")
    parser.add_argument("-s", "--savefig", help = "Save the figure.", 
                        action = "store_true")
    parser.add_argument("-St", "--saveTitle", help = "File name to save \
the plot as.", default = "PLOT")
    parser.add_argument("-T", "--title", help = "Plot title.", default = "PLOT")
    parser.add_argument("-d", "--display", help = "Disply the plots or \
not - default=True", action = "store_true")

    return parser

def to_show_or_not_to_show(savefig: bool = False, displayfig: bool = True, name: str = "PLOT") -> None:
    if displayfig:
        if not savefig:
            plt.show()
        else:   # savefig == True
            plt.savefig(f"{name}")
            plt.show()
    else:
        if not savefig:
            print("Well, ok then.")
        else:
            plt.savefig(f"{name}")

def main(argv = None):
    if argv is None:
        argv = sys.argv

    parser = create_parser()
    inputs = parser.parse_args(argv[1:])

    title = inputs.title
    datafiles = [str(i) for i in inputs.files]

    headers = ""
    scale = 1e0 # Expecting global material thickness to be in mm
    mass = []
    theta0 = []
    
    fig, ax = plt.subplots()
    # Read each file and produce plot of rho_nn and rho_n'n' vs Coord.
    d10th = 0   # This is just to set a limit on the x-axis
    for file in datafiles:
        with open(file, "r") as f:
            print(file)
            headers = f.readline()  # Get the headers and such
            catch = f.readline().split()
            mass.append(float(catch[0]))
            theta0.append(float(catch[1]))
            data = np.loadtxt(file, dtype=float, skiprows = 2, comments='#')
        f.close()   # Now it's definitely closed

        # Plot each file's data
        # header is: global x, mat. x, pnn, pmn, pnm, pmm
        # indices are:   0        1     2    3    4    5
        ax.semilogy(data[:,0] * scale, data[:,2], label = r"$\rho_{{nn}}  $; m = {}, $\theta_0$ = {}".format(mass[-1], theta0[-1]), marker = '.', ls = "dotted", c = 'red')
        ax.semilogy(data[:,0] * scale, data[:,5], label = r"$\rho_{{n'n'}}$; m = {}, $\theta_0$ = {}".format(mass[-1], theta0[-1]), marker = '.', ls = "dotted", c = 'blue')
        
        theta0.append(data[0,0])
        
    # Plot
    d10th = data[-1,0]/10
    locmin = tick.LogLocator(base=10.0, subs=(0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9), numticks=12)
    ax.yaxis.set_minor_locator(locmin)
#    ax.yaxis.set_minor_formatter(tick.NullFormatter())
    ax.grid(True, which='both')
    plt.tick_params(axis='y', which='minor')
    #ax.set_xlim([-d10th*scale,(data[-1,0] + d10th)*scale])
    ax.set_xlabel(r"$x$ (mm)")
    ax.set_ylabel(r"$\rho_{nn}$ and $\rho_{n'n'}$")
    ax.legend(loc="upper right")
    plt.title(r"$\rho_{{nn}}$ & $\rho_{{n'n'}}$")

    to_show_or_not_to_show()
    #plt.show()

if __name__ == "__main__":
    main()
