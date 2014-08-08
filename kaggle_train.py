#!/usr/bin/env python

import fileinput
from sklearn.ensemble import *
from sklearn.cross_validation import cross_val_score
from sklearn.externals import joblib
from itertools import izip
import os, sys
import dio

def io():
    target = []
    train = []

    for iline in dio.io():
        iline = iline.strip().split(',')
        t = int(iline[0])
        v = map(float, iline[1:])

        target.append(t)
        train.append(v)

    return target, train 

def train(n_estimators = 100, **kwargs):
    target, train = io()

    clf = RandomForestRegressor(n_jobs=-1, n_estimators=n_estimators, **kwargs)
    clf.fit(train, target)
    p_target = clf.predict(train)

    for a, b in izip(target, p_target):
        print a, ',', b
        #print ','.join(map(str, [a, b[1]]))
     
    joblib.dump(clf, 'train.pkl')

if __name__ == "__main__":
    dio.now('train')
