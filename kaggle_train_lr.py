#!/usr/bin/env python
from sklearn.ensemble import *
from sklearn.cross_validation import cross_val_score
from sklearn.externals import joblib
from sklearn.grid_search import GridSearchCV
from itertools import izip
import os, sys
from dpipe import dio
from sklearn.metrics import fbeta_score, make_scorer
from sklearn.feature_extraciton.text import HashingVectorizer
from kaggle_evl import *
import random
from scipy.sparse import csr_matrix, hstack
from sklearn.linear_model import LogisticRegression


def io():
    hv = HashingVectorizer()

    target = []
    train_int = []
    train_label = []

    for iline in dio.io():
        iline = iline.strip().split(',')
        t = int(iline[0])
        int_fs = map(int, iline[1:14])
        label_fs = iline[14:]

        target.append(t)
        train_int.append(int_fs)
        train_label.append(label_fs)

    train_int = csr_matrix(train_int)
    train_label = hv.transform(train_label)
    train = hstack(train_int, train_label)

    return target, train

def train():
    target, train = io()

    lr = LogisticRegression()
    lr.fit(train, target)
    p = lr.predict_proba(train)

    for i in p:
        print i

if __name__ == "__main__":
    dio.now()


