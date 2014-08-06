#!/usr/bin/env python

import fileinput
from sklearn import preprocessing
from sklearn.externals import joblib

def label():
    vs = []
    for iline in fileinput.input():
        iline = iline.strip().split(',')
        vs.append(iline)

    le = preprocessing.LabelEncoder()
    le.fit_transform(vs)

    
