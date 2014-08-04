#!/usr/bin/env python

from sklearn.preprocessing import Imputer
from sklearn import preprocessing
import scipy.sparse as sp
import fileinput
import numpy


def imputer():
    train = []
    for iline in fileinput.input():
        iline = iline.strip().split(',')
        try:
            train.append([float(x) if x else numpy.NaN for x in iline])
        except:
            pass

    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
#    print train
#    train = sp.csc_matrix(train)
    imp.fit(train[:10000])
    results = []
    while train:
        results.extend(imp.transform(train[:10000]))
        del train[:10000]

    #train = [imp.transform(train[k:k+10000]) for k in xrange(0, len(train), 10000)] 
    #train = imp.transform(train)
#    train = preprocessing.scale(results)

#    h, w =  train.shape

#    for index in xrange(h):
#        iline = train.getrow(index).toarray()[0]
    for iline in train:
        print ",".join(map(str, iline))

if __name__ == "__main__":
    imputer()
