#!/usr/bin/env python
from sklearn.preprocessing import Imputer
import fileinput

def imputer():
    train = []
    for iline in fileinput.input():
        iline = iline.strip().split(',')
        try:
            train.append([float(x) if x else numpy.NaN for x in iline])
        except:
            pass

    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imp.fit(train)
    train = imp.transform(train)
    for iline in train:
        print list(iline)

if __name__ == "__main__":
    imputer()
