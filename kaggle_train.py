#!/usr/bin/env python

import fileinput
from sklearn.ensemble import *
from sklearn.cross_validation import cross_val_score
from sklearn.externals import joblib
from itertools import izip
import os, sys
from dpipe import dio
from scipy.sparse import *

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

    #print ri+1, max(col)
    return train, csr_matrix((data, (row, col)), shape=(ri+1, max(col)+1))


def io():
    target = []
    train = []

    for iline in dio.io():
        iline = iline.strip().split(',')
        t = int(iline[0])
        v = map(int, iline[1:])

        k = v[:13] + [0] * 987
        ls = v[13:]
        ls.sort()
        for l in ls:
            if l+13 < 1000:
                k[l+13] = 1

#        print v[:13], ls, k
        target.append(t)
        train.append(k)

#    print target, train
    return target, train


def train(model, n_estimators = 100, **kwargs):
    target, train = io()
#    print target
    clf = RandomForestRegressor(n_jobs=-1, n_estimators=n_estimators, **kwargs)
    clf.fit(train, target)
    p_target = clf.predict(train)

    for a, b in izip(target, p_target):
        print a, ',', b

    joblib.dump(clf, model)


def predict(model):
    clf = joblib.load(model)

    ids, tests = io()

    p_test = []
    while tests:
        p_test.extend( clf.predict(tests[:10000]))
        del tests[:10000]

    for a, b in izip(ids, p_test):
        print ','.join(map(str, [a, b[1]]))

if __name__ == "__main__":
    dio.now()
