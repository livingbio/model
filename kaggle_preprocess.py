#!/usr/bin/env python
from collections import Counter
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
from sklearn.decomposition import PCA
import scipy.sparse as sp
import fileinput
import numpy
from itertools import izip
from dpipe import dio


def imputer():
    vs = []
    for iline in dio.io():
        iline = iline.strip().split(',')
        vs.append([int(x) if x else numpy.NaN for x in iline])

    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    vs = imp.fit_transform(vs)

    for v in vs:
        print ",".join(map(str, map(int, v)))


def scale(feature_range=(-128, 127), **kwargs):
    vs = []
    for iline in dio.io():
        iline = iline.strip().split(',')
        vs.append(map(int, iline))

    imp = MinMaxScaler(feature_range, **kwargs)
    vs = imp.fit_transform(vs)

    for v in vs:
        print ",".join(map(str, map(int, v)))


def label_transform(model):
    c = {}
    with open(model) as ifile:
        for iline in ifile:
            label, mark = [k.strip() for k in iline.split(',')]
            c[label] = int(mark)

    for iline in dio.io():
        iline = iline.strip().split(',')

        print ','.join(map(str, [c[k] for k in iline if k in c]))


def label_train(model, threshold=0.1):
    vs = []
    c = Counter()

    for iline in dio.io():
        iline = iline.strip().split(',')
        c.update(iline)

        vs.append(iline)

    c.pop('')
    if isinstance(threshold, int):
        threshold = threshold
    elif isinstance(threshold, float):
        threshold = int(len(c) * threshold)
    else:
        raise

    c = {label: index for index, (label, freq) in enumerate(c.most_common()[:threshold])}

    with open(model, 'w') as ofile:
        for label in c:
            print >> ofile, label, ',', c[label]

    for iline in vs:
        print ','.join(map(str, [c[k] for k in iline if k in c]))


if __name__ == "__main__":
    dio.now()
