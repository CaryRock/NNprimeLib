from setuptools import find_packages, setup

setup(
        name            = 'NNprimeLib',
        packages        = find_packages(include = ["NNprimeLib"]),
        version         = '0.3.3',
        description     = "Collection of convenience scripts for analyzing N-N' simulation data.",
        author          = "Cary Rock",
        license         = "GPL3",
        install_requires= ["numpy", "matplotlib"],
        setup_requires  = ["pytest-runner"],
        tests_rquire    = ["pytest == 4.4.1"],
        test_suite      = "tests",
        scripts         = ["bin/analyze_nnp_data.py", 
                            "bin/plot_rho_vs_theta.py", 
                            "bin/plot_rho_coord.py",
                            "bin/color_log_plot.py"]
)
