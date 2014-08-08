#!/usr/bin/env python

import fileinput
from sklearn.ensemble import *
from sklearn.cross_validation import cross_val_score
from sklearn.externals import joblib
from itertools import izip
import os, sys
import dio

def sparse_io():
    row = []
    col = []
    data = []
    target = []

    for ri, iline in enumerate(dio.io()):
        iline = iline.strip().split(',')
        t = int(iline[0])
        irow = map(int, iline[1:])

        target.append(t)

        for ci, v in enumerate(irow[:13]):
            row.append(ri)
            col.append(ci)
            data.append(v)

        for l in irow[13:]:
            row.append(ri)
            col.append(l+13)
            data.append(1)

    return csr_matrix((data, (row, col)), sharp=(ri, max(col)))


def io():
    target = []
    train = []

    for iline in dio.io():
        iline = iline.strip().split(',')
        t = int(iline[0])
        v = map(int, iline[1:])

        target.append(t)
        train.append(v)

    return target, train


def train(n_estimators = 100, **kwargs):
    target, train = sparse_io()

    clf = RandomForestRegressor(n_jobs=-1, n_estimators=n_estimators, **kwargs)
    clf.fit(train, target)
    p_target = clf.predict(train)

    for a, b in izip(target, p_target):
        print a, ',', b

    joblib.dump(clf, 'train.pkl')

if __name__ == "__main__":
    dio.now('train')
