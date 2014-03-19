#!/usr/bin/env python

import glob
from datetime import datetime
import numpy as np
from netCDF4 import Dataset, num2date, date2num
from scipy.interpolate import RectBivariateSpline

class Value(object):

    def __init__(self, data, title, units, dims, dim_names, latlon, limits, latlon_limits):
        self.data = data
        self.title = title
        self.units = units
        self.dims = dims
        self.dim_names = dim_names
        self.latlon = latlon
        self.limits = limits
        self.latlon_limits = latlon_limits

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
