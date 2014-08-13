#!/usr/bin/env python
from sklearn.ensemble import *
from sklearn.cross_validation import cross_val_score
from sklearn.externals import joblib
from sklearn.grid_search import GridSearchCV
from itertools import izip
import os, sys
from dpipe import dio
from sklearn.metrics import fbeta_score, make_scorer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction import FeatureHasher
from kaggle_evl import *
import random
from scipy.sparse import csr_matrix, hstack
from sklearn.linear_model import LogisticRegression
import numpy
from sklearn.preprocessing import Imputer
from sklearn import preprocessing

def io():
    hv = FeatureHasher()

    target = []
    train_int = []
    train_label = []

    for iline in dio.io():
        iline = iline.strip().split(',')
        t = int(iline[0])
        int_fs = map(lambda i: numpy.NaN if not i else int(i), iline[1:14])
        label_fs = [k for k in iline[14:]]
        #label_fs = ",".join(iline[14:])
#        print int_fs, label_fs

        target.append(t)
        train_int.append(int_fs)
        train_label.append({k:1 for k in label_fs})

#    print train_int
    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    train_int = imp.fit_transform(train_int)
#    print train_int
    scaler = preprocessing.StandardScaler().fit(train_int)
    train_int = scaler.transform(train_int)
#    print train_int
    train_int = csr_matrix(train_int)
#    print train_label
    train_label = hv.transform(train_label)
    train = hstack((train_int, train_label))
#    print train_label
#    print train
    return target, train

def train(model):
    target, train = io()

    lr = LogisticRegression()
    lr.fit(train, target)
    p = lr.predict_proba(train)

    for a, i in izip(target, p):
        print a, ',', i[1]

    joblib.dump(lr, model)


def predict(model):
    clf = joblib.load(model)
    ids, tests = io()

    while tests:
        results = clf.predict_proba(tests[:10000])

        for a, b in izip(ids, results):
            print a, ',', b

        del ids[:10000]
        del tests[:10000]

if __name__ == "__main__":
    dio.now()


