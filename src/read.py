#!/usr/bin/env python

class Reader(object):

    def __init__(self, pattern):
        self._files = []
        self._ds = []
        for f in sorted(glob.glob(pattern)):
            self._files.append(f)
            self._ds.append(Dataset(f))

class RegCMReader(Reader):
    pass

class CRUReader(Reader):
    pass