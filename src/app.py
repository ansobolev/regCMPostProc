#!/usr/bin/env python

import sys
#from read import Reader
from plot import Plotter

class Reader(object):
    pass

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print "usage: ./app.py 'model_file_pattern' model_nc_variable 'observ_glob_pattern' observ_nc_variable"
        sys.exit(1)
    pattern = sys.argv[1]
    nc_var = sys.argv[2]
    obs_pattern = sys.argv[3]
    obs_nc_var = sys.argv[4]

    r = Reader(pattern)
    value = r.get_value(nc_var)
    limits = value.get_limits()

    obs_r = Reader(obs_pattern)
    obs_value = r.get_value(obs_nc_var, limits = limits)

    value.regrid(obs_value.grid)
    diff = abs(obs_value - value)
    plt = Plotter()

    plt.plot(diff.mean())