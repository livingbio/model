#!/usr/bin/env python

import fileinput
from sklearn.ensemble import *
from sklearn.cross_validation import cross_val_score
from sklearn.externals import joblib
from sklearn.grid_search import GridSearchCV
from itertools import izip
import os, sys
from dpipe import dio
from sklearn.metrics import fbeta_score, make_scorer
from kaggle_evl import *

def kaggle_score(act, predict):
    return llfun(act, predict)

scorer = make_scorer(kaggle_score, greater_is_better=False)

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

        target.append(t)
        train.append(k)

    return target, train


def fake(value=None, **kwargs):
    target, train = io()

    if value==None:
        g = lambda: random.random()
    elif isinstance(value, float):
        g = lambda: 0 if random.random() < value else 1
    else:
        g = lambda: value

    for a in target:
        print a, ',', g()


def grid_search(model):
    target, train = io()
    forest = RandomForestRegressor(n_jobs=-1)
    parameters = {
        "n_estimators":[10, 50, 100, 200],
        "bootstrap" = [True, False],
        "min_samples_split"= [1],
        "max_depth"=[None],
        "max_features"=["auto", None]
    }
    clf = grid_search.GridSearchCV(forest, parameters, scoring=scorer, n_jobs=-1)
    clf.fit(train, target)

    print clf.best_score_
    joblib.dump(clf, model)


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

    while tests:
        results =  clf.predict(tests[:10000])

        for a, b in izip(ids, results):
            print a, ',', b

        del ids[:10000]
        del tests[:10000]


if __name__ == "__main__":
    dio.now()
