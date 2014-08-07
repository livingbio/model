#!/usr/bin/env python

from sklearn.preprocessing import Imputer
from sklearn import preprocessing
from sklearn.decomposition import PCA
import scipy.sparse as sp
import fileinput
import numpy
from itertools import izip
import dio
    
def imputer():
    target = []
    train = []

    for iline in dio.io():
        iline = iline.strip().split(',')
        t = int(iline[0])
        v = [(float(x) if x else numpy.NaN) for x in iline[1:]]
	
        target.append(t)
        train.append(v)

    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    train = imp.fit_transform(train)
    train = preprocessing.scale(train)

#    pca = PCA(whiten=False)
#    train = pca.fit_transform(train)

    for itarget, itrain in izip(target, train):
        print itarget, ',',
        print ",".join(map(str, itrain))

if __name__ == "__main__":
#     import clime.now
    dio.now('imputer')
