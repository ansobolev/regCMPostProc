#!/usr/bin/env python

class Reader(object):

    def __init__(self, pattern):
        self._files = []
        self._ds = []
        for f in sorted(glob.glob(pattern)):
            self._files.append(f)
            self._ds.append(Dataset(f))

    def _get_latlon_limits(self):
        latlon_limits = {}
        # in hope that all datasets have the same latitude and longitude points
        ds = self._ds[0]
        for crd, crd_name in self.crd_names.iteritems():
            crd_value = ds.variables[crd_name][:]
            latlon_limits[crd] = [np.min(crd_value), np.max(crd_value)]
        return latlon_limits


class RegCMReader(Reader):
    crd_names = {'lat': 'xlat', 'lon': 'xlon'}

class CRUReader(Reader):
    crd_names = {'lat': 'lat', 'lon': 'lon'}
