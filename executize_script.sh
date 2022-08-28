#!/bin/sh
# This script makes sure that the relevant scripts *are* executable. Cloud
# storage disabling that (reasonably) and all that.

for x in analyze_nnp_data.py plot_rho_coord.py plot_rho_vs_theta.py; do
    chmod +x $HOME/.local/bin/$x
done

printf "Done\n"
