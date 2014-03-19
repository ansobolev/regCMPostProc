#!/usr/bin/env python

import glob
from datetime import datetime
import numpy as np
from netCDF4 import Dataset, num2date, date2num
from scipy.interpolate import RectBivariateSpline

class Value(object):

    def __init__(self, data=None, title=None, units=None, dims=None, 
                       dim_names=None, latlon=None, limits=None, latlon_limits=None):
        self.data = data
        self.title = title
        self.units = units
        self.dims = dims
        self.dim_names = dim_names
        self.latlon = latlon
        self.limits = limits
        self.latlon_limits = latlon_limits

    def update(self, value):
        # title update only if value is empty
        if self.title is None:
            self.title = value.title
        else:
            assert self.title == value.title
        # the same goes with units
        if self.units is None:
            self.units = value.units
        else:
            assert self.units == value.units
        # and with dim_names
        if self.dim_names is None:
            self.dim_names = value.dim_names
        else:
            assert self.dim_names == value.dim_names
        # and with latlon
        if self.latlon is None:
            self.latlon = value.latlon
        else:
            assert np.all(self.latlon[0] == value.latlon[0])
            assert np.all(self.latlon[1] == value.latlon[1])
        # and with latlon_limits
        if self.latlon_limits is None:
            self.latlon_limits = value.latlon_limits
        else:
            assert self.latlon_limits == value.latlon_limits
        # data(over time axis), dims(time) and limits(time) should be expanded
        if self.data is None:
            self.data = value.data
        else:
            # hope that time axis is 0 (can check for it in dims)
            self.data = np.vstack((self.data, value.data))
        # dims
        if self.dims is None:
            self.dims = value.dims
        else:
            # also hope that time axis is 0
            self.dims[0] = np.hstack((self.dims[0], value.dims[0]))
        # limits
        if self.limits is None:
            self.limits = value.limits
        else:
            # hope that time goes increasing
            self.limits['time'] = [self.limits['time'][0], value.limits['time'][1]]

    def get_limits(self, name):
        return self.limits[name]

    def get_latlonlimits(self):
        return self.latlon_limits

    def mean(self):
        self.data = np.mean(self.data, axis=0)

    def __sub__(self, other):
        assert self.data.shape == other.data.shape
        return Value(self.data - other.data, self.title, self.units, self.dims, self.dim_names, self.latlon, self.limits, self.latlon_limits)

    def __abs__(self):
        return Value(np.abs(self.data), self.title, self.units, self.dims, self.dim_names, self.latlon, self.limits, self.latlon_limits)

class Temperature(Value):

    def to_C(self):
        self.data -= 273.15

    def to_K(self):
        self.data += 273.15
