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

    def _get_latlon_within_limits(self, latlon_limits):
        # in hope that all datasets have the same latitude and longitude points
        latlon = []
        ds = self._ds[0]
        for crd in ['lat', 'lon']:
            crd_name = self.crd_names[crd]
            crd_value = ds.variables[crd_name][:]
            crd_shape = crd_value.shape
            min_crd, max_crd = latlon_limits[crd]
            crd_idx = np.where((crd_value >= min_crd) & (crd_value <= max_crd))
            latlon.append(crd_value[crd_idx].reshape(crd_shape))
        return latlon

class CRUReader(Reader):
    crd_names = {'lat': 'lat', 'lon': 'lon'}

    def _translate_latlon_limits(self, latlon_limits):
        # in CRU file a variable depends on actual lat and lon
        for limit in latlon_limits.keys():
            assert limit in self.crd_names.keys()
        return latlon_limits

    def _get_latlon_within_limits(self, latlon_limits):
        # in hope that all datasets have the same latitude and longitude points
        latlon = []
        ds = self._ds[0]
        for crd in ['lat', 'lon']:
            crd_name = self.crd_names[crd]
            crd_value = ds.variables[crd_name][:]
            min_crd, max_crd = latlon_limits[crd]
            crd_idx = np.where((crd_value >= min_crd) & (crd_value <= max_crd))
            latlon.append(crd_value[crd_idx])
        lat, lon = np.meshgrid(latlon[0], latlon[1])
        return [lat.T, lon.T]

