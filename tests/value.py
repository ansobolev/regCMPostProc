
#!/usr/bin/env python

import glob
from datetime import datetime
import numpy as np
from netCDF4 import Dataset, num2date, date2num
from scipy.interpolate import RectSphereBivariateSpline

class n_value(reader):
    def __init__(self, names,unit, data, grid,time):
        self.names = reader.var_names
        self.unit = reader.var_unit
	self.data = reader.var_date
	self.grid = reader.var_grid
        self.time = reader.var_time

    def regrid(self,xlan,xlon):
	old_xlan = self.grid[0]
        old_xlon = self.grid[1]
        old_xlan, old_xlon = np.meshgrid(old_xlan,old_xlon)
        lut = RectSphereBivariateSpline(lats, lons, data)
        self.data = lut.ev(old_lats.ravel(),old_lons.ravel()).reshape((360, 180)).T

    def m_average(names,data,times):
        fdate = datetime.date(times[0])
        edate = datetime.date(times[1])
        ac = fdate.isocalendar()
        bc = edate.isocalendar()
  	alist = []
  	blist = []
  	for i in ac:
      	    alist.append(i)

  	for j in bc:
      	    blist.append(j)

  	lcount = [0]
   	j = 0
  	count = 0
        maverage = []
        temp = []
  	while alist[0] <= blist[0]:
        	if alist[0] == blist[0] and alist[1] == blist[1] and alist[2] == blist[2]:
           	   break
        	while  alist[2] <= 11:
               	       d1 = datetime.date(alist[0], alist[2], alist[1])
               	       alist[2] += 1
                       d2 = datetime.date(alist[0], alist[2], alist[1])
                       diff = (d2 -d1).days
		       for i in range(1,diff+1):
                   	   lcount.append(i)
                   	   count = count + diff
                           chunk = lcount[0:diff]
                temp = llcount.append(chunk)
                
        	alist[2] = 1
        	alist[0] += 1
		m_mean = np.mean(self.data[temp], axis=0)
                maverage.append(m_mean)
        return maverage
           
    def y_m_average(names,data, times):
        m_mean = np.mean(self.data[data][times], axis=0)
        return m_mean

    def y_average(names,date,grid):


    def t_average(names,date,grid):



