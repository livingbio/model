#!/usr/bin/env python

from sklearn.preprocessing import Imputer
from sklearn import preprocessing
import scipy.sparse as sp
import fileinput
import numpy
from itertools import izip
    
def imputer():
    target = []
    train = []

    for iline in fileinput.input():
        iline = iline.strip().split(',')
        t = int(iline[0])
        v = [(float(x) if x else numpy.NaN) for x in iline[1:]]
	
        target.append(t)
        train.append(v)

    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
#    print train
#    train = sp.csc_matrix(train)
    imp.fit(train)
    train = imp.transform(train)
    #results = []
    #while train:
    #    results.extend(imp.transform(train[:10000]))
    #    del train[:10000]

    #train = results
    #train = [imp.transform(train[k:k+10000]) for k in xrange(0, len(train), 10000)] 
    #train = imp.transform(train)
    train = preprocessing.scale(train)

#    h, w =  train.shape

#    for index in xrange(h):
#        iline = train.getrow(index).toarray()[0]
    for itarget, itrain in izip(target, train):
        print itarget, ',',
        print ",".join(map(str, itrain))

if __name__ == "__main__":
    imputer()
