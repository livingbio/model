#!/usr/bin/env python
from sklearn.preprocessing import Imputer
from sklearn import preprocessing
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
    imp.fit(train)
#    print train
    train = imp.transform(train)
    train = preprocessing.scale(train)

#    print train

    for iline in train:
        print ",".join(map(str, iline))

if __name__ == "__main__":
    imputer()
