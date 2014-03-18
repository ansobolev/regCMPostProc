
#!/usr/bin/env python

import glob
from datetime import datetime
import numpy as np
from netCDF4 import Dataset, num2date, date2num

class Reader(object):

    def __init__(self, ptn, var_names, limits=None):
        self.names = var_names
        self.var = {name:[] for name in self.names}
        if limits is not None:
            self.limits = limits
        else:
            self.limits = {}
        for f in sorted(glob.glob(ptn)):
            print f
            ds = Dataset(f)
            if 'time' in self.limits.keys():
                time = ds.variables['time']
                try:
                    calendar = time.calendar
                except:
                    calendar = 'gregorian'
                self.limits['time'] = date2num(self.limits['time'], units=time.units, calendar=calendar)
                print self.limits['time']
            for name in self.names:
                for k
                self.var[name].append(ds.variables[name][:])

if __name__ == "__main__":
    r_mod = Reader('data/*.2010*.nc', ['xlat', 'xlon', 'tpr'])
    d =  np.array(r_mod.var['tpr'])
    lat = (np.min(r_mod.var['xlat'][0]), np.max(r_mod.var['xlat'][0]))
    lon = (np.min(r_mod.var['xlon'][0]), np.max(r_mod.var['xlon'][0]))
    time = [datetime(2002, 01, 01), datetime(2002, 12, 31)]
#    d_mean = np.mean(d, axis=1)
#    print d_mean.shape
    r_obs = Reader('obs/CRUTMP.CDF', ['lat', 'lon', 'TMP'], limits={'lat':lat, 'lon':lon, 'time':time})
    print r_obs.var['lat'][0]
