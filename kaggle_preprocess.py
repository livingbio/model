#!/usr/bin/env python

from sklearn.preprocessing import Imputer
from sklearn import preprocessing
from sklearn.decomposition import PCA
import scipy.sparse as sp
import fileinput
import numpy
from itertools import izip
from dpipe import dio

def imputer():
    vs = []
    for iline in dio.io():
        iline = iline.strip().split(',')
        vs.append([int(x) if x else numpy.NaN for x in iline])

    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    vs = imp.fit_transform(vs)

    for v in vs:
        print ",".join(map(str, map(int, v)))

if __name__ == "__main__":
    dio.now('imputer')
