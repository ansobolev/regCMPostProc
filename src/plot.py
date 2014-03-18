#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from value import Value

class Plotter(object):

    def __init__(self, value):
        self._value = value
        self.lat, self.lon = value.grid

    def plot(self, coastlines=True,
                   countries=True,
                   places=True):
        ax = plt.axes(projection=projection)

        if coastlines:
            ax.coastlines('10m')
        if countries:
            countries = cfeature.NaturalEarthFeature(
                        scale='110m', category='cultural', name='admin_0_countries')
            ax.add_feature(countries, color='r', alpha=0.1)
        if places:
            places = cfeature.NaturalEarthFeature(
                        scale='110m', category='cultural', name='populated_places')
            ax.add_feature(places, color='b', hatch='o')

        ax.contourf(self.lon, self.lat, self.value, transform=ccrs.PlateCarree(),cmap='spectral')

        # To mask out OCEAN or LAND
        #ax.add_feature(cfeature.OCEAN)
        #ax.add_feature(cfeature.LAND)

        ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                        linewidth=1, color='blue', alpha=0.5, linestyle='-')

        times = self._value.limits['time']

        plt.title(self._value.name + ' [' + self._value.unit + ']\n' +
                        'mean between ' + str(times[0]) + ' and ' + str(times[1]) + '\n')
        plt.show()

if __name__ == "__main__":
    pass