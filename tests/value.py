
#!/usr/bin/env python

import glob
from datetime import datetime
import numpy as np
from netCDF4 import Dataset, num2date, date2num
from scipy.interpolate import RectSphereBivariateSpline

class n_value(reader):
    def __init__(self, names,unit, data, grid,time):
        self.names = var_names
        self.unit = var_unit
	self.data = var_date
	self.grid = var_grid
        self.time = var_time

    def regrid(self,xlan,xlon):
	old_xlan = self.grid[0]
        old_xlon = self.grid[1]
        old_xlan, old_xlon = np.meshgrid(old_xlan,old_xlon)
        lut = RectSphereBivariateSpline(lats, lons, data)
        self.data = lut.ev(old_lats.ravel(),old_lons.ravel()).reshape((360, 180)).T

    def m_average(names,data, times):
        m_mean = np.mean(data, names,axis=1)
           

    def y_average(names,date,grid):


    def t_average(names,date,grid):



