#!/usr/bin/env python

import sys
from read import RegCMReader, CRUReader
from plot import Plotter


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print "usage: ./app.py 'model_file_pattern' model_nc_variable 'observ_glob_pattern' observ_nc_variable"
        sys.exit(1)
    pattern = sys.argv[1]
    nc_var = sys.argv[2]
    obs_pattern = sys.argv[3]
    obs_nc_var = sys.argv[4]

    r = RegCMReader(pattern)
    value = r.get_value(nc_var).mean()
    time_limits = value.get_limits('time')
    crd_limits = value.get_latlonlimits()

    obs_r = CRUReader(obs_pattern)
    obs_value = r.get_value(obs_nc_var, imposed_limits={'time': time_limits}, latlon_limits=crd_limits).mean()
    if obs_nc_var == "TMP":
        obs_value.to_K()

    value.regrid(obs_value.latlon)
    diff = abs(obs_value - value)
    plt = Plotter(diff)
    plt.plot()
    plt.show()
    plt.save('image', format='png')
    plt.close()
